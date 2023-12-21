
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    primes = []
    for num in nums:
        if num < 10:
            continue
        digits = str(num)
        if '0' in digits:
            continue
        prime = True
        for i in range(len(digits)):
            if not is_prime(int(digits[i:])):
                prime = False
                break
            if not is_prime(int(digits[:len(digits)-i])):
                prime = False
                break
        if prime:
            primes.append(num)
    primes.sort(reverse=True)
    return primes
