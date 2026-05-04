import csv
import math
from dataclasses import dataclass
from typing import *
import sys
sys.setrecursionlimit(10_000)

expected_headers = ["country", "year",
                    "electricity_and_heat_co2_emissions",
                    "electricity_and_heat_co2_emissions_per_capita",
                    "energy_co2_emissions",
                    "energy_co2_emissions_per_capita",
                    "total_co2_emissions_excluding_lucf",
                    "total_co2_emissions_excluding_lucf_per_capita"]


# Put your data definitions first!
@dataclass (frozen=True)
class Row:
    country:str
    year:int
    electricity_and_heat_co2_emissions:float|None
    electricity_and_heat_co2_emissions_per_capita:float|None
    energy_co2_emissions:float|None
    energy_co2_emissions_per_capita:float|None
    total_co2_emissions_excluding_lucf:float|None
    total_co2_emissions_excluding_lucf_per_capita:float|None

@dataclass (frozen=True)
class Node:
    value:Row
    next: Node|None = None

# ...

# Then your functions.
def read_csv_lines(filename: str) -> Optional[Node]:
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        if header != expected_headers:
            return None
        return list_builder(reader)


def list_builder(reader) -> Optional[Node]:
    try:
        remaining_fields = next(reader)
        return Node(parse_row(remaining_fields), list_builder(reader)) #recursive case
    except StopIteration: #had to read up on csv documentation and file reading, 101 briefly touched on this
        return None

def parse_row(fields: list[str]) -> Row:

    new_row = Row(fields[0], int(fields[1]), float_specializer(fields[2]),
                  float_specializer(fields[3]), float_specializer(fields[4]), float_specializer(fields[5]),
                  float_specializer(fields[6]), float_specializer(fields[7]))

    return new_row

def float_specializer(s:str) -> float | None:
    if s != "":
        return float(s)
    else:
        return None

def listlen(data: Optional[Node]) -> int:
    pass

# ...
