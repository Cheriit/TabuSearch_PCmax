# TabuSearch solver

Simple TabuSearch solver for P|C|max issue. 

## Requirements

```
    python -m venv env
    source env/bin/activate
    pip install -r requirements.txt
```

## Running instance generator

```
    python generator.py <instance name> <CPU number> <process count> [ <min process len> <max process len> ]
```

## Running solver
Running all instances in `data` directory
```
    ./start.sh
```
Running specific instance from `data` directory. If there's no name, script will download example instance from url specified in `config.ini` file
```
    ./python main.py [<name>]
```

## Configuration

All configuration is in `config.ini` file.
- `url` - default instance url
- `defaultFilename` - default instance name after save
- `dataDir` - directory with instances
- `minProcessLen` - default minimum generated process length
- `maxProcessLen` - default minimum generated process length
- `generations` - number of TabuSearch generations
- `tabu_len` - length of tabu list
- `divider` - ignored maximal/minimal values in search
