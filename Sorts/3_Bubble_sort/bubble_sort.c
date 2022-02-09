#include <stdio.h>

// Best Case Time Complexity: O(n). Best case occurs when array is already sorted.
// Worst Case Time Complexity: O(n^2). Worst case occurs when array is reverse sorted.
// Average Case Time Complexity: O(n^2)
// Stable
void bubble_sort(int *arr, int arr_size){
    for(int i=0; i < arr_size-1 ; i++){
        for(int j=0; j < arr_size-i-1 ; j++){
            if(arr[j] > arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}


// The above function always runs O(n^2) time even if the array is sorted. It can be optimized by stopping the algorithm if inner loop didn’t cause any swap. 
void bubble_sort_optimized(int *arr, int arr_size){
    for(int i=0; i < arr_size-1 ; i++){
        int swap_happened = 0;
        for(int j=0; j < arr_size-i-1; j++){
            if(arr[j] > arr[j+1]){
                swap_happened =1;
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }

        if(swap_happened ==0){
            break;
        }
    }
}


void print_arr(int *arr, int arr_size){
    for(int i=0; i < arr_size; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
}
int main(){
    int array[] = {1, 56, 2, 10, 8};
    int array_size = sizeof(array) / sizeof(array_size);

    bubble_sort_optimized(array, array_size);
    
    print_arr(array, array_size);
    return 0;
}