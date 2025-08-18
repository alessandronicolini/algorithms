from typing import List
from enum import Enum, unique, auto
from utils import Order
import operator


def insertion_sort(arr: List[int], ascending: bool = True) -> None:
    
    if ascending:
        comp = (lambda x, y: x > y)
    else:
        comp = (lambda x, y: x <= y)

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

    insertion_sort(arr, ascending = False)
    print("INPUT SORTED (DESC order)")
    print(f"arr{arr}")
