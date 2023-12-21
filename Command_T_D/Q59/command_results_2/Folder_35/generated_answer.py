def all_left_truncatable_prime(nums):
    x = nums[177]
    l = []
    for i in range(2, x // 2):
        s = str(i)
        while s[0] == '0':
            s = s[1:]
        if len(s) == 0 or s[0] == '1':
            continue
        if s[-1] == '9':
            continue
        if not i % 2:
            continue
        if s[0] == '5' and s[1] == '0':
            continue
        l.append(i)
    l.sort()
    return l
