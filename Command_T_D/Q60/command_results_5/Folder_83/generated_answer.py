
def all_left_right_truncatable_prime(nums):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    for i in range(24, nums[0] + 1):
        for p in primes:
            if p <= i:
                if is_left_right_truncatable_prime(p, i):
                    primes.append(p)
                    break
            else:
                break
    return primes

def is_left_right_truncatable_prime(p, i):
    while len(str(p)) > 1:
        if str(p)[0] == '0' or str(p)[-1] == '0':
            return False
        p = int(str(p)[1:-1])
    return True
