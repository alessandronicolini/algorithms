from typing import List
from enum import Enum, unique
import operator

@unique
class Order(Enum):
    ASC = 0
    DESC = 1

def selection_sort(arr: List[int], ord = Order.ASC) -> None:
    m_value: int
    m_pos: int
    temp: int
    
    if ord == Order.ASC:
        comp = operator.lt
    else:
        comp = operator.gt

    for i in range(len(arr) - 1):
        m_value = arr[i]
        m_pos = i
        for j in range(i + 1, len(arr)):
            if comp(arr[j], m_value):
                m_value = arr[j]
                m_pos = j
        temp = arr[i]
        arr[i] = m_value
        arr[m_pos] = temp


if __name__ == "__main__":

    arr = [2, 4, 5, 9, 2, 10, -1, 8]
    print("PROBLEM INPUT:")
    print(f"arr{arr}")
    print()

    selection_sort(arr)
    print("INPUT SORTED (ASC order):")
    print(f"arr{arr}")
    print()

    selection_sort(arr, Order.DESC)
    print("INPUT SORTED (DESC order):")
    print(f"arr{arr}")
    print()
