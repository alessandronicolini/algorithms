from typing import List
from enum import Enum, unique, auto
import operator

@unique
class Order(Enum):
    ASC = auto()
    DESC = auto()


def insertion_sort(arr: List[int], ord = Order.ASC):
    
    if ord == Order.ASC:
        comp = operator.gt
    else:
        comp = operator.lt

    for j in range(1, len(arr)):
        
        key = arr[j]
        i = j - 1

        while i >= 0 and comp(arr[i], key):
            arr[i + 1] = arr[i]
            i = i - 1

        arr[i + 1] = key


if __name__ == "__main__":

    arr = [2, 4, 5, 9, 2, 10, -1, 8]
    print("PROBLEM INPUT")
    print(f"arr{arr}")
    print()

    insertion_sort(arr)
    print("INPUT SORTED (ASC order)")
    print(f"arr{arr}")
    print()

    insertion_sort(arr, Order.DESC)
    print("INPUT SORTED (DESC order)")
    print(f"arr{arr}")
