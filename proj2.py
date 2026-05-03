import csv
import math
from dataclasses import dataclass
from typing import *


# Put your data definitions first!
@dataclass (frozen=True)
class Row:
    line:str

@dataclass (frozen=True)
class Node:
    value:Row
    next: Node|None = None
    #
# ...

# Then your functions.

# ...
