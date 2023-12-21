
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[975]
    primes = []
    for i in range(2, x+1):
        if all(map(lambda c: c != '0' and is_prime(int(c)), [str(i)[j:] for j in range(len(str(i)))])):
            primes.append(i)
    primes.sort(reverse=True)
    return primes
