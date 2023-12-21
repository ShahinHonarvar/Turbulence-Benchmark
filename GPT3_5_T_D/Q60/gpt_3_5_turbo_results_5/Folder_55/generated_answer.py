
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[73]
    primes = []
    for num in range(x, 0, -1):
        str_num = str(num)
        if '0' not in str_num:
            prime = True
            for i in range(len(str_num)):
                left_trunc = int(str_num[i:])
                right_trunc = int(str_num[:len(str_num)-i])
                if not is_prime(left_trunc) or not is_prime(right_trunc):
                    prime = False
                    break
            if prime:
                primes.append(num)
    primes.sort(reverse=True)
    return primes
