from typing import List
from datetime import datetime


def radix_sort(arr: List) -> List:
    max_ = max(arr)
    digits = 1
    max_ //= 10
    while max_:
        max_ //= 10
        digits += 1
    rad_bucket = [[] for _ in range(10)]
    for i in range(digits):
        for j in arr:
            if i > 0:
                count = (j % (10**(i+1))) // (10**i)
                rad_bucket[count].append(j)
            else:
                rad_bucket[j % 10].append(j)
        arr = []
        k = 0
        while k < len(rad_bucket):
            if rad_bucket[k]:
                arr.extend(rad_bucket[k])
                rad_bucket[k] = []
            k += 1
    return arr


# arr = [10, 0, 2, 4, 9, 67, 815]
abc_ = 10**2000
before = datetime.now()
arr = [10, 0, 2, 4, 9, 500, 2000, 67, 815]
arr = radix_sort(arr)
after = datetime.now()
print(arr)
print(f"time taken: {after-before}")

