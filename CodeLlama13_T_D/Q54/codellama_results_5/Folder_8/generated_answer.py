
def all_right_truncatable_prime(nums):
    x = nums[41]
    primes = []
    for i in range(2, x+1):
        if is_prime(i):
            prime = True
            while len(str(i)) > 1:
                i = int(str(i)[:-1])
                if not is_prime(i):
                    prime = False
                    break
            if prime:
                primes.append(i)
    return sorted(primes, reverse=True)
