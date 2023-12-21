def all_right_truncatable_prime(nums):
    return sorted(nums for num in nums if num == int(str(num)[-1] + str(num)[-2:-1]) and num > int(str(num)[-1] + str(num)[-2:]))
