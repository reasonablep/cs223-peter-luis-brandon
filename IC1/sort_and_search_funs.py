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
# Selection Sorting (iterative)
def selection_sort_iter(arr, key=None, reverse=False):
    if key is None:
        key = lambda x: x

    n = len(arr)

    for i in range(n - 1):
        selected_index = i

        for j in range(i + 1, n):
            if reverse:
                if key(arr[j]) > key(arr[selected_index]):
                    selected_index = j
            else:
                if key(arr[j]) < key(arr[selected_index]):
                    selected_index = j

        arr[i], arr[selected_index] = (
            arr[selected_index],
            arr[i]
        )

    return arr

# Selection Sorting (recursive)
def selection_sort_recur(arr, key=None, reverse=False):
    if key is None:
        key = lambda x: x

    def sort_recursive(start_index):
        n = len(arr)

        # Base case
        if start_index >= n - 1:
            return

        selected_index = start_index

        for i in range(start_index + 1, n):
            if reverse:
                if key(arr[i]) > key(arr[selected_index]):
                    selected_index = i
            else:
                if key(arr[i]) < key(arr[selected_index]):
                    selected_index = i

        arr[start_index], arr[selected_index] = (
            arr[selected_index],
            arr[start_index]
        )

        sort_recursive(start_index + 1)

    sort_recursive(0)

    return arr

#  Quick Sort Recursive version
def quick_sort_recursive(lst, key=lambda x: x, reverse=False):
    if len(lst) <= 1: # Base case: a list of length 0 or 1 is already sorted
        return lst
    else:
        pivot = lst[0]
        pivot_val = key(pivot) # Extract the comparison value using the key function
        less = []
        greater = []
        
        for i in lst[1:]:
            i_val = key(i) # Extract the comparison value for the current element
            
            # Compare based on the reverse flag
            if i_val >= pivot_val if reverse else i_val <= pivot_val:
                less.append(i)
            else:
                greater.append(i)
                
        # Recursively sort and combine, forwarding the key and reverse arguments
        return (quick_sort_recursive(less, key, reverse) 
                + [pivot] 
                + quick_sort_recursive(greater, key, reverse))


# Quick Sort Iterative version
def partition(arr, low, high, key=lambda x: x, reverse=False): # Helper function for the iterative quicksort
    i = low - 1 # Index of smaller element
    pivot = arr[high] # Choose the last element as the pivot
    pivot_val = key(pivot)

    for j in range(low, high): # Traverse through all elements in the current subarray
        j_val = key(arr[j])
        if j_val >= pivot_val if reverse else j_val <= pivot_val: # Compare each element to the pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # Swap elements

    arr[i + 1], arr[high] = arr[high], arr[i + 1] # Swap the pivot element with the element at index i + 1
    return i + 1


def quick_sort_iterative(arr, key=lambda x: x, reverse=False):
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

        p = partition(arr, low, high, key, reverse)

        if p - 1 > low:
            stack.append(low)
            stack.append(p - 1)

        if p + 1 < high:
            stack.append(p + 1)
            stack.append(high)

    return arr

def insertion_sort_iter(arr, key=lambda x: x, reverse=False):
    n = len(arr)
    for i in range(1, n):
        current_item = arr[i] 
        current_val = key(current_item)
        j = i - 1
        
        # Move elements that don't match the sort order to one position ahead
        while j >= 0 and (key(arr[j]) < current_val if reverse else key(arr[j]) > current_val):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_item
    return arr

def insertion_sort_recur(arr, n=None, key=lambda x: x, reverse=False):
    if n is None:
        n = len(arr)
        
    # Base case: already sorted
    if n <= 1:
        return arr
        
    # Sort first n-1 elements
    insertion_sort_recur(arr, n - 1, key, reverse)
    
    # Insert the last element at its correct position in the sorted array
    last_item = arr[n - 1]
    last_val = key(last_item)
    j = n - 2
    
    while j >= 0 and (key(arr[j]) < last_val if reverse else key(arr[j]) > last_val):
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = last_item
    
    return arr
