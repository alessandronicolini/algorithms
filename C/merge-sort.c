#include <stdio.h>
#include "utils.h"
#include <stdbool.h>

#define N 10

void 
merge(int *arr, int l_idx, int m_idx, int r_idx, bool ascending)
{
    // define left array
    int left_len = m_idx - l_idx + 1;
    int left_arr[left_len];
    for (int i = 0; i < left_len; i++) {
        left_arr[i] = arr[l_idx + i];
    }

    // define right subarray
    int right_len = r_idx - (m_idx + 1) + 1;
    int right_arr[right_len];
    for (int i = 0; i < right_len; i++) {
        right_arr[i] = arr[m_idx + 1 + i];
    }

    // merge the two subarrays into the original one
    // while mantaining the starting range
    int i = 0;
    int j = 0;
    int k = l_idx;

    // while both subarrays have elements
    while (i < left_len && j < right_len) { 
        if (
            (ascending && left_arr[i] <= right_arr[j]) || 
            (!ascending && left_arr[i] > right_arr[j])
        ){
            arr[k++] = left_arr[i++];
        } else {
            arr[k++] = right_arr[j++];
        }
    }  
    
    // complete pushing the remaining element if any
    while (i < left_len) {
        arr[k++] = left_arr[i++];
    }

    while (j < right_len) {
        arr[k++] = right_arr[j++];
    }
}

void
merge_sort(int *arr, int l_idx, int r_idx, bool ascending)
{
    if (r_idx - l_idx == 0) return;

    int m_idx = (r_idx - l_idx) / 2 + l_idx;
    merge_sort(arr, l_idx, m_idx, ascending);
    merge_sort(arr, m_idx + 1, r_idx, ascending);
    merge(arr, l_idx, m_idx, r_idx, ascending);
}

int 
main(void)
{   
    bool asc_order = true;
    bool desc_order = !asc_order;

    int arr[N] = {2, 3, -3, 6, 5, -5, 10, 32, 4, 8};
    printf("PROBLEM INPUT:\n");
    print_array(arr, N);

    printf("\n");
    
    printf("INPUT SORTED (ASC order):\n");
    merge_sort(arr, 0, N - 1, asc_order); 
    print_array(arr, N);

    printf("\n");

    printf("INPUT SORTED (DESC order):\n");
    merge_sort(arr, 0, N - 1, desc_order);
    print_array(arr, N);
}
