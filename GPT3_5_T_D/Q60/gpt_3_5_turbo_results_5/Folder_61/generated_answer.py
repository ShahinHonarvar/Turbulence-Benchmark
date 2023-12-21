
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    prime_nums = []
    for num in nums:
        if num < 10:
            continue
        if is_prime(num):
            str_num = str(num)
            if '0' in str_num:
                continue
            is_left_right_truncatable_prime = True
            while len(str_num) > 1 and is_left_right_truncatable_prime:
                if not is_prime(int(str_num)):
                    is_left_right_truncatable_prime = False
                str_num = str_num[1:-1]
            if is_left_right_truncatable_prime:
                prime_nums.append(num)
    return sorted(prime_nums, reverse=True)
