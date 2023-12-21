
def all_left_right_truncatable_prime(nums):
    l = nums[760]
    if l < 2:
        return []
    s = set(str(l))
    for n in range(l - 1, 1, -1):
        if str(n) in s:
            continue
        s.add(str(n))
        break
    for n in range(l + 1, len(str(l)) + 1):
        if str(n) in s:
            continue
        s.add(str(n))
        break
    return [int(n) for n in s]
