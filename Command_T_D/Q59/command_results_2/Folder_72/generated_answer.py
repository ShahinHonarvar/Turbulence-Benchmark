import sys
def all_left_truncatable_prime(x):
    def check(i):
        # find all left-truncatable primes
        for j in range(2, x+1):
            if i%10 != j:
                continue
            if i < j:
                break
            for k in range(10):
                if i%10 == k:
                    break
                if i < k:
                    continue
                if j%10 == k:
                    break
                if j < k:
                    continue
                if k == 0 or k == 9:
                    continue
                if j > i:
                    break
                elif j == i:
                    return True
                elif i > j:
                    break
                elif i == j:
                    return True
        return False
    # return all left-truncatable primes
    return [n for n in range(2, x+1) if all(check(n) for _ in range(10))]
