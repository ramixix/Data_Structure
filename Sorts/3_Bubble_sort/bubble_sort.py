def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]


def bubble_sort_optimized(arr):
    for i in range(len(arr)-1):
        swap_happened = False
        for j in range(len(arr)-i-1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_happened = True

        if not swap_happened:
            break


array = [1, 56, 2, 10, 8]
print("Array before sorting :")
for i in array:
    print(i, end=" ")

bubble_sort(array)

print("\nArray after sorting:")
for i in array:
    print(i, end=" ")

