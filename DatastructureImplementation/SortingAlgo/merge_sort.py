from datetime import datetime


def arr_concat(arr1, arr2):
    i = j = 0
    out = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            out.append(arr1[i])
            i += 1
        else:
            out.append(arr2[j])
            j += 1
    while i < len(arr1):
        out.append(arr1[i])
        i += 1
    while j < len(arr2):
        out.append(arr2[j])
        j += 1
    return out


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    m = len(arr) // 2
    arr1 = merge_sort(arr[:m])
    arr2 = merge_sort(arr[m:])
    return arr_concat(arr1, arr2)


before = datetime.now()
arr = [10, 0, 2, 4, 9, 500, 2000, 67, 815]
arr = merge_sort(arr)
after = datetime.now()
print(arr)
print(f"time taken: {after-before}")