
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(nums):
    x = nums[126]
    primes = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            truncatable_prime = True
            temp = num
            while temp > 0:
                if not is_prime(temp):
                    truncatable_prime = False
                    break
                temp = temp // 10
            if truncatable_prime:
                primes.append(num)
    return sorted(primes, reverse=True)
