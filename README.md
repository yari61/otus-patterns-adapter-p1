# Initialization
## Clone project
```
git clone https://github.com/yari61/otus-patterns-adapter-p1.git
cd otus-patterns-adapter-p1
```

## Virtual environment
It is recommended to create a virtual environment at first (.venv for example)
```
python -m venv .venv
```

Then activate it with 
- ```source .venv/bin/activate```
on Unix-like systems, or
- ```.venv\Scripts\activate```
if Your system runs Windows

## Installation
To install the package run the next command in your virtual environment
```
pip install -e .
```

## Testing
To run tests execute the command listed below
```
python -m unittest
```

# Project description
## Goal
The main goal of this program is to load two matrices from the input file, summarize them, and dump a result matrix to the output file.