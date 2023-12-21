
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    primes = []
    for num in nums:
        if is_prime(num):
            str_num = str(num)
            if '0' not in str_num:
                is_truncatable = True
                for i in range(1, len(str_num)):
                    trunc_num = int(str_num[:i])
                    if not is_prime(trunc_num):
                        is_truncatable = False
                        break
                for i in range(len(str_num) - 1, 0, -1):
                    trunc_num = int(str_num[i:])
                    if not is_prime(trunc_num):
                        is_truncatable = False
                        break
                if is_truncatable:
                    primes.append(num)
    return sorted(primes, reverse=True)
