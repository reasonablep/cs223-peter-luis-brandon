# Helper function

def merge(left, right, key, reverse=False):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if reverse:
            take_left = key(left[i]) >= key(right[j])
        else:
            take_left = key(left[i]) <= key(right[j])

        if take_left:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Recursive

def merge_sort_recursive(A, key=lambda x: x, reverse=False):
    if len(A) <= 1:
        return A.copy()

    mid = len(A) // 2
    left = merge_sort_recursive(A[:mid], key, reverse)
    right = merge_sort_recursive(A[mid:], key, reverse)

    return merge(left, right, key, reverse)

# Iterative

def merge_sort_iterative(A, key=lambda x: x, reverse=False):
    result = A.copy()
    n = len(result)
    width = 1

    while width < n:
        for start in range(0, n, 2 * width):
            mid = min(start + width, n)
            end = min(start + 2 * width, n)

            result[start:end] = merge(
                result[start:mid],
                result[mid:end],
                key,
                reverse
            )

        width *= 2

    return result

# Iterative Selection Sort 
def selection_sort_iter(arr):
    n = len(arr)
    # Loop through the entire array except the last element
    for i in range(n - 1): # 
        # Assume the current position holds the minimum value
        min_index = i
        
        # Scan the remaining unsorted region to find the actual minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        # Swap the found minimum element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return arr

# Recursive Selection Sort
def selection_sort_recur(arr, start_index=0):
    n = len(arr)
    
    # Base Case: If we have reached the last element, the array is sorted
    if start_index >= n - 1:
        return
    
    # Find the index of the minimum element in the unsorted sub-array
    min_index = start_index
    for i in range(start_index + 1, n):
        if arr[i] < arr[min_index]:
            min_index = i
            
    # Swap the found minimum element with the first element of this sub-array
    arr[start_index], arr[min_index] = arr[min_index], arr[start_index]
    
    # Recursively sort the remaining elements
    selection_sort_recur(arr, start_index + 1)
