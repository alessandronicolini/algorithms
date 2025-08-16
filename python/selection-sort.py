from typing import List
from enum import Enum, unique
from utils import Order


def selection_sort(arr: List[int], ascending: bool = True) -> None:
    """Implements the Selection Sort algorithm. 

    The input array is split into two subarrays:
        - left subarray: ordered
        - right subarray: unordered
    
    The i index points to the current element that should be inserted
    in the ordered subarray and moves from left to right.
    The unordered subarray is scanned to find its min (max) value
    which is swapped with the element pointed by i.
    The ordered subarray grows by one element, the unordered subarray
    shrinks by one element, i is incremented and the process repeats until
    the whole array is sorted.

    Note that the comparison operator that decides the sorting order,
    ascending or descending, can be determined since the beginning.

    Parameters
    ----------
    arr : List[int]
        The array that is sorted in place

    ascending : bool, optional
        The sorting order, if False the array is sorted in descending
        order, otherwise ascending. Default is True.
    """
    m_pos: int
    
    if ascending:
        comp = (lambda x, y: x < y)
    else:
        comp = (lambda x, y: x > y)

    for i in range(len(arr) - 1):
        m_pos = i
        for j in range(i + 1, len(arr)):
            if comp(arr[j], arr[m_pos]):
                m_pos = j

        arr[i], arr[m_pos] = arr[m_pos], arr[i]


if __name__ == "__main__":

    arr = [2, 4, 5, 9, 2, 10, -1, 8]
    print("PROBLEM INPUT:")
    print(f"arr{arr}")
    print()

    selection_sort(arr)
    print("INPUT SORTED (ASC order):")
    print(f"arr{arr}")
    print()

    selection_sort(arr, ascending = False)
    print("INPUT SORTED (DESC order):")
    print(f"arr{arr}")
    print()
