
def all_left_truncatable_prime(nums):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    x = nums[92]
    primes = []

    for i in range(2, x):
        if '0' not in str(i):
            prime = True
            for j in range(len(str(i))):
                if not is_prime(int(str(i)[j:])):
                    prime = False
                    break
            if prime:
                primes.append(i)

    return sorted(primes)
