def all_right_truncatable_prime(n):
    # sort all primes less than n
    # and then return all those that are right truncatable
    l = []
    for i in range(2, n[0] // 2):
        if all(str(i).count(d) == 1 for d in range(str(i).count("0"))):
            l.append(i)
    return sorted(set(l), reverse=True)
