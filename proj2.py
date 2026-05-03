import csv
import math
from dataclasses import dataclass
from typing import *


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
    pass

def parse_rows(fields: list[str]) -> Row:

    def float_specializer(s:str) -> float | None:
        if s != "":
            return float(s)
        else:
            return None

    new_row = Row(fields[0], int(fields[1]), float_specializer(fields[2]),
                  float_specializer(fields[3]), float_specializer(fields[4]), float_specializer(fields[5]),
                  float_specializer(fields[6]), float_specializer(fields[7]))

    return new_row

# ...
