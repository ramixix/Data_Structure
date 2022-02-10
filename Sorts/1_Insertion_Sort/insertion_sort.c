#include <stdio.h>


// Best Case Time Complexity [Big-omega]: O(n)
// Worst Case Time Complexity [ Big-O ]: O(n^2)
// Average Time Complexity [Big-theta]: O(n^2)
// stable

// method with two for loop
void insertion_sort(int *arr, int arr_size){
	
	for(int i = 1; i < arr_size; i++){
		for(int j=i; j > 0; j--){
			if(arr[j] < arr[j-1]){
				int temp = arr[j];
				arr[j] = arr[j-1];
				arr[j-1] = temp;
			}
		}
	}
}

// method with one for and one while loop
void insertion_sort1(int *arr, int arr_size){
	for(int i=1; i < arr_size; i++){
		int key = arr[i];
		int j = i-1;
		while(key < arr[j] && j >= 0){
			arr[j+1] = arr[j];
			j-=1;
		}
		arr[j+1] = key;
	}
}


// print the array to stdout.
void print_arr(int *arr, int arr_size){
	for(int i = 0; i < arr_size; i++){
		printf("%d ", arr[i]);
	}
	printf("\n");
}


int main(){
	int arr[] = {1, 56,2,10, 8};
	int arr_size = sizeof(arr) / sizeof(arr[0]);

	insertion_sort1(arr, arr_size);
	print_arr(arr, arr_size);
	
	return 0;
}