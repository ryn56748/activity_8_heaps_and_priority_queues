def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        _heapify(arr, i, 0)
        
    return arr

def _heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)

print("\n Activity 3 ")
print("Test 1 [4, 10, 3, 5, 1]:", heap_sort([4, 10, 3, 5, 1]))
print("Already sorted [1, 2, 3, 4, 5]:", heap_sort([1, 2, 3, 4, 5]))
print("Reverse sorted [5, 4, 3, 2, 1]:", heap_sort([5, 4, 3, 2, 1]))
print("With duplicates [4, 2, 4, 1, 2]:", heap_sort([4, 2, 4, 1, 2]))
print("Empty array []:", heap_sort([]))