def all_right_truncatable_prime(nums):
    res = []
    for i in range(3, int(str(nums[0])[0])))[::-1]:
        for j in range(3, int(str(nums[0])[0])))[::-1]:
            for d in range(3, str(nums[0])[0]):
                if str(i**2 + j)[:-1] == str(i**2 + j + 1):
                    res.append(i**2 + j)
    return res
