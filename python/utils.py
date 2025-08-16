from enum import Enum, unique

@unique
class Order(Enum):
    ASC = 0
    DESC = 1
