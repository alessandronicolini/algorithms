#include <stdio.h>
#include "utils.h"

#define N 8

void selection_sort(int *arr, int n, Order ord) {

    int m_value, m_pos, temp;

    for (int i = 0; i < n - 1; i++) {

        // initialize the m_value with the first element
        // of the unordered subarray
        m_value = arr[i];
        m_pos = i;
        
        // loop over the right unordered subarray and find the m (min or max)
        // according the sorting order
        if (ord == ORDER_ASC) {
            for (int j = i + 1; j < n; j++) {
                if (arr[j] < m_value) {
                    m_value = arr[j];
                    m_pos = j;
                }
            }
        } else {
            for (int j = i + 1; j < n; j++) {
                if (arr[j] > m_value) {
                    m_value = arr[j];
                    m_pos = j;
                }
            }
        }
        
        // exchange the found m value with the first element of
        // the current right unordered subarray.
        // The left ordered subarray grow by 1 element while the 
        // right unordered subarray shrink by 1 element.
        temp = arr[i];
        arr[i] = m_value;
        arr[m_pos] = temp;
    }
}

int main(void) {
    int arr[N] = {3, 5, 2, 7, 8, -2, -5, 6};
    printf("PROBLEM INPUT:\n");
    print_array(arr, N);
    printf("\n");

    selection_sort(arr, N, ORDER_ASC);
    printf("SORTED (ASC order):\n");
    print_array(arr, N);
    printf("\n");

    selection_sort(arr, N, ORDER_DESC);
    printf("SORTED (DESC order):\n");
    print_array(arr, N);
}
