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

#  Quick Sort Recursive version
def quick_sort_recursive(lst, descending=False):
    if len(lst) <= 1: # Base case: a list of length 0 or 1 is already sorted
        return lst
    else:
        pivot = lst[0] # Choose the first element as the pivot
        less = []
        greater = []
        for i in lst[1:]: # Compare each element to the pivot and partition the list into two sublists
            if i >= pivot if descending else i <= pivot:
                less.append(i) 
            else:
                greater.append(i)
        return quick_sort_recursive(less, descending) + [pivot] + quick_sort_recursive(greater, descending)

# Quick Sort Iterative version
def partition(arr, low, high, descending=False): # Helper function for the iterative quicksort
    i = low - 1 # Index of smaller element
    pivot = arr[high] # Choose the last element as the pivot
    
    for j in range(low, high): # Traverse through all elements in the current subarray
        if arr[j] >= pivot if descending else arr[j] <= pivot: # Compare each element to the pivot and partition the list into two sublists
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # Swap elements
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1] # Swap the pivot element with the element at index i + 1
    return i + 1


def quick_sort_iterative(arr, descending=False):
    if len(arr) <= 1: 
        return arr

    low = 0
    high = len(arr) - 1
    stack = []
    
    stack.append(low) 
    stack.append(high)
    
    while stack: # Continue until the stack is empty
        high = stack.pop()
        low = stack.pop()
        
        p = partition(arr, low, high, descending)

        if p - 1 > low:
            stack.append(low)
            stack.append(p - 1)

        if p + 1 < high:
            stack.append(p + 1)
            stack.append(high)

    return arr
