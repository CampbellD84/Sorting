# STRETCH: implement Linear Search
def linear_search(arr, target):
    for idx in range(0, len(arr)):
        if arr[idx] == target:
            return idx

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high) // 2
        if target < arr[mid]:
            # get rid of right hand side
            high = mid-1
        elif target > arr[mid]:
            # get rid of left hand side
            low = mid+1
        else:
            return mid

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    mid = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty

    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        return binary_search_recursive(arr[:mid], target, 0, len(arr[:mid]))
    else:
        return binary_search_recursive(arr[mid:], target, 0, len(arr[mid:])-1)
