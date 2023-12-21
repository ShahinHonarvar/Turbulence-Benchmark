def all_left_truncatable_prime(nums):
    lst = []
    for i in range(2, int(nums[61]) + 1):
        str_num = str(i)
        if str_num[0] != '0' and all(str_num[j] == '0' for j in range(1, len(str_num))):
            lst.append(i)
    return sorted(lst)
