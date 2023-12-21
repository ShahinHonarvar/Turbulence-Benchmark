
def all_left_right_truncatable_prime(nums):
    # your code here
    lst = []
    for i in range(2, nums[33]):
        d = str(i)
        cnt = 0
        for j in range(len(d)):
            if d[j] == '0':
                break
            else:
                cnt += 1
        if cnt > 1:
            lst.append(i)
    return lst
