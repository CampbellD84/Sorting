# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # init an empty list
    merged_arr = []
    # set index to 0
    idx = jdx = 0

    # loop while index is < len of [A] and j index is < len of [B]
    while idx < len(arrA) and jdx < len(arrB):
        # if A[idx] is < B[jdx]
        if arrA[idx] < arrB[jdx]:
            # append A[idx] to merged_arr
            merged_arr.append(arrA[idx])
            # increment idx
            idx += 1
        else:
            # append B[jdx] to merged_arr
            merged_arr.append(arrB[jdx])
            # increment jdx
            jdx += 1
    # merge lists
    merged_arr += arrA[idx:]
    merged_arr += arrB[jdx:]

    return merged_arr


def merge_sort(arr):
    # if list len is < 2
    if len(arr) < 2:
        # return list
        return arr
    # find middle of list
    midArr = len(arr) // 2
    # split list from beginning to middle
    arrL = merge_sort(arr[:midArr])
    # spilt list from middle to end
    arrR = merge_sort(arr[midArr:])

    # merge list
    return merge(arrL, arrR)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
