# Stock Trading with Gym Environment
A custom OpenAI gym environment for simulating stock trades on historical price data.

## Installation of Stable_Baselines

### Prerequisites
Baselines requires python3 (>=3.5) with the development headers. You'll also need system packages CMake, OpenMPI and zlib. Those can be installed as follows

#### Mac OS X
Installation of system packages on Mac requires [Homebrew](https://brew.sh). With Homebrew installed, run the follwing:
```bash
brew install cmake openmpi
```
### Install using pip
Install the Stable Baselines package

Using pip from pypi:
```
pip install stable-baselines
```

Please read the [documentation](https://stable-baselines.readthedocs.io/) for more details and alternatives (from source, using docker).

## Installation of mpl_finance
Install the mpl_finance package for plotting

Using pip from pypi:
```
pip install mpl_finance
```

## How to run

### Get historical data
To get historical stock price data from Alpha Vantage, run the following code:
```
python fetchdata.py
```

### Run the algorithm
You can either render the result to a text file or visualize it
```
python main.py
```
Check the parameter of the render function for usage.

## References

If you'd like to learn about creating custom OpenAI gym environments, 
check out the [Medium article](https://medium.com/@adamjking3/creating-a-custom-openai-gym-environment-for-stock-trading-be532be3910e)
