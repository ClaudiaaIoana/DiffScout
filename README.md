# DiffScout

**DiffScout** is a Python library designed for automated differential cryptanalysis of SPN (Substitution-Permutation Network) ciphers. By blending symbolic artificial intelligence with cryptanalytic expertise, DiffScout introduces a fresh approach to discovering and evaluating differential characteristics in symmetric cryptographic primitives.

---

## Solution description

DiffScout changes the game by:

- Leveraging the **A\*** search algorithm guided by a smart, simulation-based **MCTS-inspired heuristic**.
- Exploring differential paths as optimal trees instead of static constraint sets.
- Dramatically reducing search space through **equivalent difference detection**.
- Enabling discovery of **pseudo-iterative differential characteristics** that extend known cryptanalytic results.

---

## Features

- **Automated Path Discovery**: Automatically finds optimal differential trails using A\* search.
- **Heuristic Intelligence**: Custom heuristic inspired by Monte Carlo Tree Search simulations.
- **Equivalent Difference Detection**: Identifies structurally similar differences to streamline the analysis.
- **Pseudo-Iterative Characteristics**: Extracts and extends useful patterns not documented in existing literature.
- **Cipher Support**: Includes analysis modules for:
  - `PRESENT`
  - `GIFT-64`
  - `RECTANGLE`

## Installation

You can install **DiffScout** in a Python environment using `pip`.

### Prerequisites

Make sure you have:

- Python 3.7 or later
- `pip` (Python package manager)

---

### Install from local directory

```bash
# Navigate to the root directory of the project

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# Install the package in editable mode
pip install -e .
