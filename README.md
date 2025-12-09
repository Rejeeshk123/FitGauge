# FitGauge

A small collection of Monte Carlo simulations for classic probability puzzles. Run the CLI to explore outcomes for the birthday paradox or the Monty Hall problem.

## Setup

The simulations use only the Python standard library. Any modern Python 3 interpreter will work.

## Usage

### Birthday paradox
Estimate how often at least two people in a group share a birthday.

```bash
python math_simulation.py birthday --group-size 23 --trials 20000
python math_simulation.py birthday --group-size 23 --trials 20000 --seed 1234
```

### Monty Hall problem
See how often switching doors wins compared to staying with the initial choice.

```bash
python math_simulation.py monty --switch --trials 20000
python math_simulation.py monty --stay --trials 20000
python math_simulation.py monty --switch --trials 20000 --seed 1234
```

### Reproducibility
Add the optional `--seed` flag to any command to make the simulation results reproducible.

### Testing
Run the automated checks with:

```bash
python -m pytest
```
