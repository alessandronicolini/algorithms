#include <stdio.h>
#include "utils.h"
#define N 10

void insertion_sort(int *arr, int n, Order order) {
    for (int j = 1; j < n; j++) {
        int key = arr[j];

        // last index of the sorted subarray
        int i = j - 1;

        // insert the current element in the sorted subarray
        // by translating the elements on the right until 
        // the insertion point is found
        // (changing > to < change the sorting order)
        if (order == ORDER_ASC) {
            while (i >= 0 && arr[i] > key) {
                arr[i + 1] = arr[i];
                i--;
            }
        } else {
            while (i >= 0 && arr[i] < key) {
                arr[i + 1] = arr[i];
                i--;
            }
        }

        arr[i + 1] = key;
    }
}

void insertion_sort_asc(int *arr, int n) {
    insertion_sort(arr, n, ORDER_ASC);
}

void insertion_sort_desc(int *arr, int n) {
    insertion_sort(arr, n, ORDER_DESC);
}

int main(void) {
    int arr[N] = {2,5,4,1,7,9,6,2,6,8};

    printf("PROBLEM INPUT:\n");
    print_array(arr, N);

    printf("\n");

    insertion_sort_asc(arr, N);
    printf("SORTED  (ASC order):\n");
    print_array(arr, N);
    
    printf("\n");

    insertion_sort_desc(arr, N);
    printf("SORTED (DESC order):\n");
    print_array(arr, N);

    return 0;
}
