#include <stdio.h>


// Best Case Complexity: O(n^2)
// Worst Case Complexity: O(n^2)
// Average Case Complexity: O(n^2)
void selection_sort(int *arr, int arr_size){
    for(int i = 0; i < arr_size-1; i++){
        int position_of_min_val = i;

        for(int j = i+1; j < arr_size; j++){
            if(arr[j] < arr[position_of_min_val]){
                position_of_min_val = j;
            }
        }

        if(position_of_min_val != i){
            int temp = arr[i];
            arr[i] = arr[position_of_min_val];
            arr[position_of_min_val] = temp;
        }
    }
}


void print_arr(int *arr, int arr_size){
    for(int i=0; i<arr_size; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main(){
    int array[] = {1, 56, 2, 10, 8};
    int array_size = sizeof(array) / sizeof(array_size);

    selection_sort(array, array_size);
    print_arr(array, array_size);
    return 0;

}