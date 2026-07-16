# freeCodeCamp Daily Challenges as Python functions

You can run these functions on local (read each function summary at the top of the file).

## Tests

For running each of these functions unit tests you may use these scripts:

### Running a Single Test File

```bash
cd dailyCodingChallenge
python -m unittest tests.test_exact_change # remember to change the file name
```

### Running All Tests

```bash
cd dailyCodingChallenge
python -m unittest discover -s tests -p "test_*.py"
```

### Verbose Output

```bash
cd dailyCodingChallenge
python -m unittest discover -s tests -p "test_*.py" -v
```

### Tests are also being run through a workflow on github actions [here](https://github.com/EmmanuelTechRD/freecodecamp/actions/workflows/test.yml).