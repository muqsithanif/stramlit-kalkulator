# stramlit-kalkulator

A lightweight multi-page Streamlit web application for calculating fundamental electrical circuit parameters and understanding circuit physics.

## Features

- **Series Circuits:** Equivalent resistance calculation ($R_s = R_1 + R_2$).
- **Parallel Circuits:** Combined parallel resistance calculation ($R_p = \frac{1}{\frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3}}$).
- **Ohm's Law Calculators:**
  - Electric Current ($I = \frac{V}{R}$)
  - Resistance ($R = \frac{V}{I}$)
  - Voltage ($V = I \cdot R$)

## Project Structure

```
stramlit-kalkulator/
├── terahir/
│   ├── main.py                    # Multi-page landing and circuit theory introduction
│   └── pages/
│       ├── Arus listrik.py        # Electric current calculator
│       ├── Hambatan lisrik.py     # Resistance calculator
│       ├── Rangkaian pararel.py   # Parallel circuit calculator
│       ├── Rangkaian seri.py      # Series circuit calculator
│       └── Tegangan listrik.py    # Voltage calculator
├── requirements.txt
└── README.md
```

## Quick Start

### 1. Installation

```bash
git clone https://github.com/muqsithanif/stramlit-kalkulator.git
cd stramlit-kalkulator

python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
```

### 2. Run the App

```bash
streamlit run terahir/main.py
```
Open your browser at `http://localhost:8501`.
