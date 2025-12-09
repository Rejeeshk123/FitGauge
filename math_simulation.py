"""Math simulations for common probability puzzles.

This module provides simple Monte Carlo simulations for two classic
problems:
- Birthday paradox: probability that at least two people in a group share a birthday.
- Monty Hall problem: advantage of switching doors after a non-prize door is revealed.

Use the CLI to run simulations and view estimated probabilities.
"""

from __future__ import annotations

import argparse
import random
from dataclasses import dataclass


@dataclass
class BirthdayParadoxResult:
    group_size: int
    trials: int
    matches: int

    @property
    def probability(self) -> float:
        """Estimated probability of at least one shared birthday."""
        return self.matches / self.trials if self.trials else 0.0


@dataclass
class MontyHallResult:
    trials: int
    wins: int
    switched: bool

    @property
    def win_rate(self) -> float:
        """Estimated win rate when using the chosen strategy."""
        return self.wins / self.trials if self.trials else 0.0


def simulate_birthday_paradox(group_size: int, trials: int, days: int = 365) -> BirthdayParadoxResult:
    """Run a Monte Carlo simulation of the birthday paradox.

    Args:
        group_size: Number of people sampled per trial.
        trials: Number of simulation iterations.
        days: Number of possible birthdays (defaults to 365).

    Returns:
        BirthdayParadoxResult containing aggregate counts and estimated probability.
    """
    matches = 0

    for _ in range(trials):
        seen = set()
        for _ in range(group_size):
            birthday = random.randint(1, days)
            if birthday in seen:
                matches += 1
                break
            seen.add(birthday)

    return BirthdayParadoxResult(group_size=group_size, trials=trials, matches=matches)


def simulate_monty_hall(trials: int, switch: bool) -> MontyHallResult:
    """Simulate the Monty Hall problem.

    Args:
        trials: Number of simulation iterations.
        switch: Whether the contestant switches after a door is revealed.

    Returns:
        MontyHallResult with aggregate win count and win rate.
    """
    wins = 0

    for _ in range(trials):
        prize_door = random.randint(1, 3)
        initial_pick = random.randint(1, 3)

        # Host reveals a goat door that is not the player's pick or the prize door.
        remaining_doors = {1, 2, 3} - {initial_pick, prize_door}
        revealed_door = random.choice(list(remaining_doors))

        final_pick = initial_pick
        if switch:
            final_pick = ({1, 2, 3} - {initial_pick, revealed_door}).pop()

        if final_pick == prize_door:
            wins += 1

    return MontyHallResult(trials=trials, wins=wins, switched=switch)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Monte Carlo simulations for classic math puzzles.")
    parser.add_argument(
        "--seed",
        type=int,
        help="Optional random seed for reproducible simulations across runs.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    birthday_parser = subparsers.add_parser("birthday", help="Simulate the birthday paradox.")
    birthday_parser.add_argument("--group-size", type=int, default=23, help="Number of people in the group (default: 23).")
    birthday_parser.add_argument("--trials", type=int, default=10000, help="Number of simulation trials (default: 10000).")
    birthday_parser.add_argument("--days", type=int, default=365, help="Number of possible birthdays (default: 365).")

    monty_parser = subparsers.add_parser("monty", help="Simulate the Monty Hall problem.")
    monty_parser.add_argument("--trials", type=int, default=10000, help="Number of simulation trials (default: 10000).")
    monty_parser.add_argument("--switch", action="store_true", help="Switch doors after the host reveals a goat.")
    monty_parser.add_argument("--stay", action="store_true", help="Stay with the initial door (overrides --switch).")

    return parser.parse_args()


def main() -> None:
    args = _parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    if args.command == "birthday":
        result = simulate_birthday_paradox(group_size=args.group_size, trials=args.trials, days=args.days)
        probability = result.probability * 100
        print(
            f"Birthday paradox: {result.group_size} people, {result.trials} trials\n"
            f"Estimated probability of shared birthday: {probability:.2f}%"
        )
    elif args.command == "monty":
        switch = args.switch and not args.stay
        result = simulate_monty_hall(trials=args.trials, switch=switch)
        win_rate = result.win_rate * 100
        strategy = "switching" if result.switched else "staying"
        print(
            f"Monty Hall: {result.trials} trials using {strategy}\n"
            f"Estimated win rate: {win_rate:.2f}%"
        )


if __name__ == "__main__":
    main()
