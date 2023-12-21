
def all_left_right_truncatable_prime(nums):
    out = []
    for i in range(2, int(nums[0])+1):
        if all(str(i).count(d) == 1 for d in str(i)):
            if i > 1 and all(str(i).count(d) == 1 for d in str(i-1)):
                if i < len(str(nums[0])) and all(str(i).count(d) == 1 for d in str(nums[0]-1)):
                    out.append(i)
    return out
