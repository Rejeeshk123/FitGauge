import random

import math_simulation


def test_birthday_paradox_reproducible_with_seed():
    random.seed(1234)
    result = math_simulation.simulate_birthday_paradox(group_size=5, trials=1000)
    assert result.matches == 23
    assert result.probability == 0.023


def test_monty_hall_switching_outperforms_staying():
    random.seed(1234)
    switching = math_simulation.simulate_monty_hall(trials=1000, switch=True)
    random.seed(1234)
    staying = math_simulation.simulate_monty_hall(trials=1000, switch=False)

    assert switching.wins == 659
    assert staying.wins == 341
    assert switching.win_rate > staying.win_rate
