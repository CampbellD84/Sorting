# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # another loop going to end of list
        for x in range(cur_index, len(arr)):
            # if item at index x is less than smallest item index
            if arr[x] < arr[smallest_index]:
                # assign smallest item index to item at index x
                smallest_index = x

        # swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # variable for length of list
    arr_len = len(arr)
    # loop through list
    for idx in range(0, arr_len):
        # another loop length of list - index from prev loop - 1
        for jdx in range(arr_len - idx - 1):
            # if item at index is greater than item at next index
            if arr[jdx] > arr[jdx + 1]:
                # swap them
                arr[jdx], arr[jdx + 1] = arr[jdx + 1], arr[jdx]

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
