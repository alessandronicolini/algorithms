#include <stdio.h>
#include "utils.h"
#include <stdbool.h>

#define N 10

void insertion_sort(int *arr, int n, bool ascending) {
    for (int j = 1; j < n; j++) {
        int key = arr[j];

        // last index of the sorted subarray
        int i = j - 1;

        // insert the current element in the sorted subarray
        // by translating the elements on the right until 
        // the insertion point is found
        // (changing > to < change the sorting order)
        while (
            i >= 0 && (
                (ascending && arr[i] > key) ||
                (!ascending && arr[i] <= key)
            )
        ) {
            arr[i + 1] = arr[i];
            i--;
        }
        
        arr[i + 1] = key;
    }
}

int main(void) {
    int arr[N] = {2,5,4,1,7,9,6,2,6,8};

    bool asc_order = true;
    bool desc_order = !asc_order;

    printf("PROBLEM INPUT:\n");
    print_array(arr, N);

    printf("\n");

    insertion_sort(arr, N, asc_order);
    printf("SORTED  (ASC order):\n");
    print_array(arr, N);
    
    printf("\n");

    insertion_sort(arr, N, desc_order);
    printf("SORTED (DESC order):\n");
    print_array(arr, N);

    return 0;
}
