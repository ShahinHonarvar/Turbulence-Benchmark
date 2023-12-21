def all_left_truncatable_prime(nums):
    return sorted(nums for num in nums if num < 10**(len(str(num)) - 1) and all(int(num[i:j]) for i in range(len(num)) for j in range(i + 1, len(num)) if all(num % x == 0 for x in range(2, int(num[i:j]) + 1)))
