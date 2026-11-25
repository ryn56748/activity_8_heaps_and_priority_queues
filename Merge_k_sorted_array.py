import heapq


def merge_k_sorted_arrays(arrays):
    min_heap = []
    result = []
    

    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], i, 0))
            
    while min_heap:
        val, arr_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)
        

        if elem_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(min_heap, (next_val, arr_idx, elem_idx + 1))
            
    return result

print("\n Activity 5 ")
arr1 = [1, 4, 7]
arr2 = [2, 5, 8, 9]
arr3 = [3, 6]
merged = merge_k_sorted_arrays([arr1, arr2, arr3])
print("Merged array:", merged)
print("Is fully sorted?", merged == sorted(arr1 + arr2 + arr3))