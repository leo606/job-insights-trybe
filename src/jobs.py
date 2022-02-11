import csv
from functools import lru_cache


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parametersclear
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path, mode="r") as file:
        data = csv.DictReader(file, delimiter=",", quotechar='"')
        return list(data)
