
def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def all_left_truncatable_prime(nums):
    x = nums[31]
    prime_list = []
    for num in range(x-1, 0, -1):
        if '0' in str(num):
            continue
        truncated_num = str(num)
        is_truncatable_prime = True
        while truncated_num:
            if not is_prime(int(truncated_num)):
                is_truncatable_prime = False
                break
            truncated_num = truncated_num[1:]
        if is_truncatable_prime:
            prime_list.append(num)
    return prime_list
