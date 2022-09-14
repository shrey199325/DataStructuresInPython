from datetime import datetime


def bubble_sort(arr):
    i, j = 0, 1
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] < arr[j]

before = datetime.now()
arr = [10, 0, 2, 4, 9, 500, 2000, 67, 815]
arr = bubble_sort(arr)
after = datetime.now()
print(arr)
print(f"time taken: {after-before}")