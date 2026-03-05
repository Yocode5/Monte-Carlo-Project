# Monte Carlo Pi Simulation

This project implements a **Monte Carlo simulation** to estimate the value of π (Pi) using random sampling techniques.

The simulation randomly generates points within a square and determines whether they fall inside the inscribed quarter circle. The ratio of points inside the circle to the total number of generated points is used to approximate π.

## Features

- Monte Carlo estimation of π
- Command-line configuration using `argparse`
- Data processing with **NumPy** and **Pandas**
- Visualization of results using **Matplotlib**
- Optional export of simulation data to **Excel**
- Improved and minimal versions of the simulation included

## Technologies Used

- Python
- argparse
- NumPy
- Pandas
- Matplotlib (pyplot)
- openpyxl

## Files

- `Mini_MonteCarlosim.py`  
  A minimal Monte Carlo simulation for estimating π.

- `MonteCarloSim_Improved.py`  
  An improved version with additional features such as data handling and visualization.

## How It Works

1. Random points are generated inside a square.
2. Each point is checked to determine whether it lies inside a quarter circle.
3. The ratio of points inside the circle is used to estimate π:

\[
\pi \approx 4 \times \frac{\text{points inside circle}}{\text{total points}}
\]

## Example Use

```bash
python MonteCarloSim_Improved.py --n 1000 10000 100000 1000000 --runs 10
