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
