# Bond Pricing

This Python module provides tools for bond valuation, including a class for representing bonds and calculating the Yield to Maturity (YTM) using the van Wijngaarden-Dekker-Brent method.

## Features

- `Bond`: A class that encapsulates bond properties and valuation methods.
- `ytm()`: A method within the `Bond` class that calculates the bond's yield to maturity.

## Installation

To use this module, simply clone the repository or download the `.py` file into your working directory.

```bash
git clone https://github.com/your-username/bond-pricing.git
```

## Usage

First, import the module and create an instance of the `Bond` class by passing in the required parameters:

```python
from bond_pricing import Bond

# Create a Bond instance
my_bond = Bond(price=950, par=1000, T=10, c=0.05, freq=2)

# Calculate the YTM
ytm_result = my_bond.ytm()
print(f"The Yield to Maturity is: {ytm_result:.2%}")
```

### Parameters:

- `price`: The current market price of the bond.
- `par`: The face value of the bond.
- `T`: The time to maturity (in years).
- `c`: The annual coupon rate (as a decimal).
- `freq`: The frequency of coupon payments per year (e.g., 2 for semi-annual).

### Methods:

- `ytm()`: Calculates the yield to maturity on the sign-changing interval [a, b], where `a = 0.01` and `b = 0.2`, as YTM values typically fall within this range.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions or requests.
