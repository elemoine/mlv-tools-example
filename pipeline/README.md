To generate the Python scripts from the Notebooks, and the DVC run scripts, for all the clients:

```shell
make all
```

For one particular client:

```shell
make one CLIENT=small-tobacco-0
```

To remove the Python scripts and the DVC run scripts for all the clients:

```shell
make cleanall
```

For one particular client:

```shell
make cleanone CLIENT=small-tobacco-0
```

**Advanced**

To generate a specific Python script (from the corresponding Notebook):

```shell
make small-tobacco-0/scripts/mlvtools_000_step0.py CLIENT=small-tobacco-0
```

To generate a specific DVC script (from the corresponding Python script):

```shell
make small-tobacco-0/dvc/mlvtools_000_step0_dvc CLIENT=small-tobacco-0
```
