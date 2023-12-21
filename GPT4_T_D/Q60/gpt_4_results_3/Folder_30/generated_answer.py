
def all_left_right_truncatable_prime(nums):
    x = nums[37]
    primes = []
    for num in range(x, 10, -1):
        str_num = str(num)
        if '0' in str_num:
            continue
        length = len(str_num)
        is_truncatable = True
        for i in range(length):
            if not (is_prime(int(str_num[i:])) and is_prime(int(str_num[:length-i]))):
                is_truncatable = False
                break
        if is_truncatable:
            primes.append(num)
    return primes

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
