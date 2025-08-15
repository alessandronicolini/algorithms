from typing import List

def insertionSort(arr: List[int]):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i = i - 1
        arr[i + 1] = key

if __name__ == "__main__":

    arr = [5, 4, 3, 2]
    print("PROBLEM INPUT")
    print(f"arr{arr}")
    print()

    insertionSort(arr)
    print("INPUT SORTED")
    print(f"arr{arr}")
