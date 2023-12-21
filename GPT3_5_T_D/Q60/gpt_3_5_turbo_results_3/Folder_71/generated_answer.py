
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    primes = []
    for i in range(len(nums)):
        if i == 22:
            x = nums[i]
    for n in range(x, 9, -1):
        if "0" not in str(n) and is_prime(n):
            left_prime = True
            right_prime = True
            left_num = str(n)
            right_num = str(n)
            while len(left_num) > 1 and left_prime:
                left_num = left_num[1:]
                if not is_prime(int(left_num)):
                    left_prime = False
            while len(right_num) > 1 and right_prime:
                right_num = right_num[:-1]
                if not is_prime(int(right_num)):
                    right_prime = False
            if left_prime and right_prime:
                primes.append(n)
    primes.sort(reverse=True)
    return primes
