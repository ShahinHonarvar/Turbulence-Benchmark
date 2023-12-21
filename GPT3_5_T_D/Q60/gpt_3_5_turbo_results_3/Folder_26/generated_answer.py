
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[81]
    primes = []
    for num in range(23, x + 1):
        if '0' in str(num):
            continue
        if is_prime(num):
            str_num = str(num)
            length = len(str_num)
            left = True
            right = True
            for j in range(1, length):
                left_num = int(str_num[j:])
                right_num = int(str_num[:-j])
                if not is_prime(left_num) or not is_prime(right_num):
                    left = False
                    break
            if left:
                primes.append(num)
    return sorted(primes, reverse=True)
