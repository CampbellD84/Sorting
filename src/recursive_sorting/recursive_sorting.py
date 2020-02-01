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
    pt1 = mid - start + 1
    pt2 = end - mid

    # temp lists
    arrL = [0] * pt1
    arrR = [0] * pt2

    # iterate through pt1
    for idx in range(0, pt1):
        arrL[idx] = arr[start + idx]

    # iterate through pt2
    for jdx in range(0, pt2):
        arrR[jdx] = arr[mid + 1 + jdx]

    # merge temp lists back into arr
    i = j = 0
    k = start

    while i < pt1 and j < pt2:
        if arrL[i] <= arrR[j]:
            arr[k] = arrL[i]
            i += 1
        else:
            arr[k] = arrR[j]
            j += 1

        k += 1

    while i < pt1:
        arr[k] = arrL[i]
        i += 1
        k += 1

    while j < pt2:
        arr[k] = arrR[j]
        j += 1
        k += 1

    return arr


def merge_sort_in_place(arr, l, r):
    if l < r:
        # dividing sum of l and r-1 in half
        md = (l+(r-1))//2

        # sort left and right halves
        merge_sort_in_place(arr, l, md)
        merge_sort_in_place(arr, md + 1, r)
        merge_in_place(arr, l, md, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
