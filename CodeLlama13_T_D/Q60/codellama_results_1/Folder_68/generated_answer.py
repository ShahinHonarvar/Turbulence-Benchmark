
def all_left_right_truncatable_prime(x):
    primes = []
    for i in range(2, x+1):
        if is_prime(i) and not contains_zero(i):
            left_truncatable = True
            right_truncatable = True
            for j in range(len(str(i))-1, 0, -1):
                if not is_prime(int(str(i)[:j])):
                    left_truncatable = False
                    break
            for j in range(2, len(str(i))+1):
                if not is_prime(int(str(i)[j:])):
                    right_truncatable = False
                    break
            if left_truncatable and right_truncatable:
                primes.append(i)
    return sorted(primes, reverse=True)
