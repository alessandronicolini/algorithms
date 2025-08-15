from typing import List
from enum import Enum, unique, auto


@unique
class Order(Enum):
    ASC = auto()
    DESC = auto()


def insertion_sort(arr: List[int], ord: Order):
    for j in range(1, len(arr)):
        
        key = arr[j]
        i = j - 1

        if ord == Order.ASC:
            while i >= 0 and arr[i] > key:
                arr[i + 1] = arr[i]
                i = i - 1
        else:
            while i >= 0 and arr[i] < key:
                arr[i + 1] = arr[i]
                i = i - 1

        arr[i + 1] = key


def insertion_sort_asc(arr: List[int]):
    insertion_sort(arr, Order.ASC)


def insertion_sort_desc(arr: List[int]):
    insertion_sort(arr, Order.DESC)


if __name__ == "__main__":

    arr = [5, 4, 3, 2]
    print("PROBLEM INPUT")
    print(f"arr{arr}")
    print()

    insertion_sort_asc(arr)
    print("INPUT SORTED (ASC order)")
    print(f"arr{arr}")
    print()

    insertion_sort_desc(arr)
    print("INPUT SORTED (DESC order)")
    print(f"arr{arr}")
