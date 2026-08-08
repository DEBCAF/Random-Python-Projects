
def insertionsort(arr):
    for i in range(1, len(arr)):
        elem = arr[i]
        j = i - 1
        while j >= 0 and elem < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = elem
    return arr

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        mergesort(left)
        mergesort(right)
    i, j, k = 0,0,0
    while i < len(left) and j < len(right):
        if left[i] < right[i]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

print(insertionsort([5, 2, 4, 6, 1, 3]))