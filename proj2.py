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
#this function uses the csv reader function to read through lines of a csv file,
#turning them into strings, which a helper function converts into floats/ints/strings
#and is attached to a Row object.
def read_csv_lines(filename: str) -> Optional[Node]:
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        if header != expected_headers:
            return None
        return list_builder(reader)

#this function places Rows into a Node and forms a linked list.
#this function doesn't have a type hint unless we import one for csv.reader
def list_builder(reader) -> Optional[Node]:
    try:
        remaining_fields = next(reader)
        return Node(parse_row(remaining_fields), list_builder(reader)) #recursive case
    except StopIteration: #had to read up on csv documentation + readme and file reading, 101 briefly touched on this
        return None

#this is a helper function that fills out the required data for each argument in the Row object
def parse_row(fields: list[str]) -> Row:

    new_row = Row(fields[0], int(fields[1]), float_specializer(fields[2]),
                  float_specializer(fields[3]), float_specializer(fields[4]), float_specializer(fields[5]),
                  float_specializer(fields[6]), float_specializer(fields[7]))

    return new_row

#this is another helper function that converts the strings from CSV to floats, and also turns blank
#spaces into None values.
def float_specializer(s:str) -> float | None:
    if s != "":
        return float(s)
    else:
        return None

#this counts the amount of country datas in a given dataset by parsing through a linked list recursively.
def listlen(data: Optional[Node]) -> int:
    # base case is if you reach the end of the linked list
    if data is None:
        return 0
    return 1 + listlen(data.next) #adds 1, and if the data isn't a none, it adds another 1

#goes through a list of data and aggregates a new linked list based on criteria, acting as a filter
def filter_rows(
    data: Optional[Node],
    field_name: str,
    comparison: str,
    value: Union[str, float, int]
    ) -> Optional[Node]:
    if data is None: #base case, where there is no data associated
        return None
    field_value = getattr(data.value, field_name) #this gets the field name in the row class

    if field_name == "country" and comparison != "equal":
        raise ValueError("countries cannot be compared and less or greater than")

    if field_value is None:
        return filter_rows(data.next, field_name, comparison, value)
    if comparer(field_value, comparison, value): #this is how it checks if the comparison is true
        return Node(data.value, filter_rows(data.next, field_name, comparison, value)) #recursive case
    else:
        return filter_rows(data.next, field_name, comparison, value)

#helper function for filter rows, where it essentially just checks for comparisons between the data
#and the comparing value
def comparer(field_value:str, comparison:str, value:Union[str, float, int]) -> bool:
    if comparison == "equal":
        return field_value == value
    elif comparison == "less_than":
        return field_value < value
    elif comparison == "greater_than":
        return field_value > value
    return False

# ...
