
def all_right_truncatable_prime(nums):
    x = nums[0]
    prime_list = []
    for i in range(10**6, 0, -1):
        if is_prime(i) and is_truncatable_prime(str(i)):
            prime_list.append(i)
        if len(prime_list) == x:
            break
    return sorted(prime_list, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(s):
    length = len(s)
    for i in range(length):
        if not is_prime(int(s[:length-i])):
            return False
    return True
