def all_right_truncatable_prime(nums):
    # code here
    lst = []
    for x in range(2, len(str(nums[91])) + 1):
        for y in range(10):
            if str(nums[91])[:x] + str(nums[91])[x-1:x+y] == str(nums[91]):
                if nums[91] % 10**(x-1-y) == 0:
                    lst.append(int(str(nums[91])[x-1:x+y]))
    return sorted(lst)
