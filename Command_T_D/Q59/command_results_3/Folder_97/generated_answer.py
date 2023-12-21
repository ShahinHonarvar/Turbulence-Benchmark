def all_left_truncatable_prime(nums):
    return sorted(
        set(
            str(i)
            for i in nums
            if all(str(i).rstrip(str(j)) in str(j) for j in nums)
        )
    )
