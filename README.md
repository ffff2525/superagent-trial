# superagent-trial
dsh-superagent trial repository

## countdown.py

`scripts/countdown.py` counts down from a positive integer `N` to `1`,
printing one number per line, and then prints `Liftoff!`:

```console
$ python scripts/countdown.py 3
3
2
1
Liftoff!
```

`N` must be a positive integer. Any other input (zero, a negative number, a
non-numeric value, …) is rejected with an explanatory error message and exit
code `2`:

```console
$ python scripts/countdown.py 0
usage: countdown.py [-h] N
countdown.py: error: expected a positive integer, got '0'
$ echo $?
2
```

Run `python scripts/countdown.py --help` for the full usage text.

### Tests

The tests use [pytest](https://pytest.org/):

```console
$ python -m pytest
```
