
def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if(arr[j] < arr[j-1]):
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp

def insertion_sort1(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while(arr[j] > key and j >= 0):
            arr[j+1] = arr[j]
            j -=1
        arr[j+1]= key

        
array = [1, 56, 2, 10, 8]
print("Array before sorting :")
for i in array:
    print(i, end=" ")

insertion_sort1(array)

print("\nArray after sorting:")
for i in array:
    print(i, end=" ")