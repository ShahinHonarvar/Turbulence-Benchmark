import bisect
def all_left_truncatable_prime(n):
    # Preprocess: create a list of left-truncatable primes
    # and their indices in the sorted list of primes
    l = [i for i in range(2, n[1] + 1) if all(int(d) for d in str(i))]
    l.sort()
    n.sort()
    indices = [0]*(len(l) + 1)
    for i in range(1, len(l)):
        indices[i] = bisect.bisect_left(n, l[i])
    # Write the function
    return n[:indices[54]]
