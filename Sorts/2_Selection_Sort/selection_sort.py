
from multiprocessing.spawn import old_main_modules


def selection_sort(arr):
    for i in range (len(arr) - 1):
        min_value_position = i
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[min_value_position]):
                min_value_position = j
        
        if(min_value_position != i):
            arr[min_value_position], arr[i] = arr[i], arr[min_value_position]



        
array = [1, 56, 2, 10, 8]
print("Array before sorting :")
for i in array:
    print(i, end=" ")

selection_sort(array)

print("\nArray after sorting:")
for i in array:
    print(i, end=" ")