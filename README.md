# Newsflash

Newsflash is a Python project for reading me the latest news while I brush my teeth or take a shower. The news themselves are taken from a [popular german news page](http://tagesschau.de). 


## Installation

In order to get started, make sure to migrate the main script to your android device and install any missing dependencies.
I recommend using [QPython](https://www.qpython.com/) for the job, as it provides a CLI for running scripts, installing dependencies, as well as an FTP server for moving files and data.

## Usage

Before you run the script, make sure to set to set your device's default language to the language of your news page. Otherwise, you are going to hear some very funny but quite incomprehensible news reports.



The script itself can be started via:
```bash
python3 main.py
```

In order to adjust the script to a different news provider and/or target language, all you need to do is change the command and text constants in the begging of the script as well as creating a new fetch function.

Have fun!

