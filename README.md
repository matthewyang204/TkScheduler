# TkScheduler
TkScheduler is a simple timer/scheduler for Tkinter, akin to PyQt's QTimer. It is designed to function similarly and I am building it mostly for use in [my own text editor written in Tkinter](https://github.com/matthewyang204/NotepadEE). However, if you want a feature, I am always open to suggestions if you get me interested enough in an idea that's practical.

## Usage
The scheduler provides two core methods: `start()` and `stop()`.

It is designed for lightweight scheduling tasks such as autosave, linting debounce, and periodic UI updates in Tkinter applications.

Available options:

| option | description | default | form                              |
|--------|------------|---------|-----------------------------------|
| root | Tkinter root instance used for scheduling | required | parameter when initializing class 
| fn | callback function executed on timeout | None | property                          |
| interval | delay in milliseconds between executions | 0 | property & parameter of start()|
| singleShotState | if True, runs only once; if False, repeats | False | property |
| isActive | returns whether a timer is currently scheduled | derived (read-only) | function that gets the internal active state |

## Installing
This software comes as a pip package hosted on PyPI.
```commandline
pip install tkscheduler
```

## License
This software is licensed under the GNU GPLv3. For more info, see the `LICENSE` file.
