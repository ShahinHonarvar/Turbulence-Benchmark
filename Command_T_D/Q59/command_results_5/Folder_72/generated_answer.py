def all_left_truncatable_prime(nums):
    return sorted(set(str(nums[31])[1:-1] for n in range(3, int(nums[31]) + 1) if n % 2 == 1 and all(str(i) for i in range(3, int(str(n) + 1) + 1) if i % 2 == 1 and all(str(j) for j in range(3, int(str(i) + 1) + 1) if j % 2 == 1 and str(n) + str(i) + str(j) == str(nums[31]))))
