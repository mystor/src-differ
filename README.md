# src-differ

Diff structure of source file asts.

## Install

```
# Create & load a virtualenv
virtualenv env
. env/bin/activate

# Install requirements
pip install -r requirements.txt

# Compare two files
python differ.py path/to/file1.py path/to/file2.py

# Also works (very very slowly) on c files
python differ.py path/to/file1.c path/to/file2.c

# Run on an entire directory!
python diffdir.py directory/containing/python/or/c/scripts
```

## Requirements
The c version uses libclang on the backend to parse the c code. If libclang isn't installed, then it probably (certainly) won't work.
