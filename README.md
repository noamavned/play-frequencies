# play-frequencies

This Python script uses the `winsound` library to play a sequence of beeps with frequencies determined by a mathematical function `f(x)`. The `play` function iterates over a range of values, computes the frequency using `f(x)`, and plays the corresponding beep sound.

## Functions

### `f(x: float) -> float`
A placeholder function for a mathematical equation that determines the frequency.

### `play(F, minLimit: float = -1, maxLimit: float = 1, jumps: float = 0.01, timeMs: int = 100, forward: bool = True)`

**Parameters**:
- `F`: The mathematical function to determine the frequency.
- `minLimit`: The starting value of the range (default is -1).
- `maxLimit`: The ending value of the range (default is 1).
- `jumps`: The step size for iterating over the range (default is 0.01).
- `timeMs`: The duration of each beep in milliseconds (default is 100).
- `forward`: Direction of iteration, forward if True (default), backward if False.

**Behavior**:
- Computes the frequency using `F(i) * 1000 + 2000`.
- Clamps the frequency to a valid range (37 Hz to 32,767 Hz).
- Plays a beep for each computed frequency over the specified range and step size.

## Usage

To use this script:

1. Define your mathematical function `f(x)`.
2. Call the `play` function with the desired parameters.

Example:
```python
def f(x):
    return x ** 2

play(f, minLimit=-1, maxLimit=1, jumps=0.05, timeMs=100, forward=True)
