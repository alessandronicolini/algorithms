#include <stdio.h>
#include "utils.h"

void print_array(int *arr, int length) {
    printf("arr[");
    for (int i = 0; i < length - 1; i++) {
        printf("%d, ", arr[i]);
    }
    printf("%d]\n", arr[length - 1]);
}
