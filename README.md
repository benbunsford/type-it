
# typeitnow

typeitnow is a terminal-based game inspired by Bop It.
As the player, you're tasked with typing in the words presented
to you before the timer runs out.
It has multiple difficulties, and can be played for fun
or to practice touch-typing.
The initial idea was to have the player press a single key,
which is more similar to Bop It.
That idea was more fun to implement, but less fun to play(to me).
Maybe I'll add it back as an option. Hope you have fun! :)

## OS

typeitnow works on Linux. It should work on Mac and Windows as well,
but has not been tested.

## Installation

1. FluidSynth (2.0.0 or later) is required. You can find instructions on how
to install it here: [FluidSynth Download](https://github.com/FluidSynth/fluidsynth/wiki/Download)
2. Install typeitnow with pip.

    ```sh
    pip install typeitnow
    ```

3. Run typeitnow in your terminal. It will automatically download `typeitnow/undertale.sf2`
to your user cache directory, which varies by OS. You can find the exact
directory in the [platformdirs documentation](https://pypi.org/project/platformdirs/),
just in case you want to delete it later.

    ```sh
    typeitnow
    ```

## TODO

- add high score tracking
- re-implement single-key mode
