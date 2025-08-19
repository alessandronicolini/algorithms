from typing import List
from math import floor

def merge (
    arr: List[int],
    l_idx: int,
    m_idx: int,
    r_idx,
    ascending: bool = True
) -> None:
    l_len = m_idx - l_idx + 1
    l_arr = [arr[i] for i in range(l_idx, m_idx + 1)]

    r_len = r_idx - (m_idx + 1) + 1
    r_arr = [arr[i] for i in range(m_idx + 1, r_idx + 1)]

    temp = None

    i, j, k = 0, 0, l_idx
    while i < l_len and j < r_len:
        if (
            (ascending and l_arr[i] <= r_arr[j]) or
            (not ascending and l_arr[i] > r_arr[j])
        ):
            arr[k] = l_arr[i]
            i += 1
            k += 1
        else:
            arr[k] = r_arr[j]
            j += 1
            k += 1

    while i < l_len:
        arr[k] = l_arr[i]
        i += 1
        k += 1

    while j < r_len:
        arr[k] = r_arr[j]
        j += 1
        k += 1



def merge_sort (
    arr: List[int],
    l_idx: int,
    r_idx: int,
    ascending: bool = True
) -> None:
    if (r_idx - l_idx == 0):
        return
    m_idx = floor((r_idx + l_idx) / 2)
    merge_sort(arr, l_idx, m_idx, ascending)
    merge_sort(arr, m_idx + 1, r_idx, ascending)
    merge(arr, l_idx, m_idx, r_idx, ascending)


if __name__ == "__main__":
    desc_order = False

    arr = [2,5,3,7,4,8,-1,-6,10,7]
    print("PROBLEM INPUT:")
    print(f"arr{arr}")
    print()

    merge_sort(arr, 0, len(arr) - 1)
    print("INPUT SORTED (ASC order):")
    print(f"arr{arr}")
    print()

    merge_sort(arr, 0, len(arr) -1, desc_order)
    print("INPUT SORTED (DESC order):")
    print(f"arr{arr}")
    print()
        
