from typing import List, Any


ZERO = 0


def operation(val1, val2):
    return val1 + val2


def build_sparse(A: List[Any]) -> List[List[Any]]:
    n = len(A)
    dp = [[0 for _ in range(n+1)] for __ in range(21)]
    for i in range(21):
        for j in range(n):
            if i == 0:
                dp[i][j] = A[j]
            else:
                dp[i][j] = operation(dp[i-1][j], dp[i - 1][min(j + (1 << (i-1)), n)])
    return dp


def query(dp, l, r):
    ans = ZERO
    if l == r:
        return dp[0][l]
    for j in range(21, -1, -1):
        if (l + (1 << j) -1) <= r:
            ans = operation(ans, dp[j][l])
            l += (1 << j)
    return ans


A = [1,1,1,1,1,1,1]
dp = build_sparse(A)
for i in dp: print(i)
Q = [[i, j] for i in range(len(A)) for j in range(i, len(A))]
# print(Q)
print(A)
for l, r in Q:
    print(f"Array -> {A[l: r+1]} == {query(dp, l, r)}")