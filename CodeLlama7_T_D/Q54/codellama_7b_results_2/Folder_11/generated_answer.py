
def all_right_truncatable_prime(nums):
    prime_list = []
    for num in nums:
        if is_prime(num):
            for i in range(1, len(str(num))):
                if is_prime(int(str(num)[:-i])):
                    prime_list.append(num)
    return sorted(prime_list)
