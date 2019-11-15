"""
To Find primes in a given range n
Complexity = O(NloglogN)
"""

def SOE(n):
    prime = [False]*2 + [True]*(n-1)
    for i in range(2, n+1):
        if prime[i]:
            j=2
            while i*j<=n:
                prime[i*j] = False
                j += 1
    for i, p in enumerate(prime):
        if p:
            print("{}".format(i), end=",")

def SOE2(n):
    res = n-1
    prime = [False] * 2 + [True] * (n - 1)
    for i in range(2, n + 1):
        if prime[i]:
            j = 2
            while i * j <= n:
                if not prime[i * j]:
                    j += 1
                    continue
                res = res-1
                prime[i * j] = False
                j += 1
    print(res)

SOE(13)
print("\n")
SOE2(13)