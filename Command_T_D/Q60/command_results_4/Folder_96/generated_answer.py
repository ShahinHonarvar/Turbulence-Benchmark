
def all_left_right_truncatable_prime(nums):
    return sorted(nums for num in range(2, int(nums[29]) + 1) if all(str(num) for str in range(str(num), str(num) + 9) if str(num) in str(num) and str(num) in str(num)[::-1] and int(str(num)) == num))
