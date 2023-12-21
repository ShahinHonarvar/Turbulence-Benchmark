
def all_left_right_truncatable_prime(nums):
    res = []
    for i in range(25, nums[0] + 1):
        x = str(i)
        if x[0] == '2' and x[-1] == '5':
            res.append(i)
            break
        elif x[0] == '2' and x[-1] == '0':
            res.append(i)
            break
        elif x[0] == '2' and x[-1] == '5' and x[1] == '0':
            res.append(i)
            break
        elif x[0] == '2' and x[1] == '5' and x[-2] == '0':
            res.append(i)
            break
        elif x[0] == '2' and x[1] == '5' and x[-2] == '0' and x[2] == '5':
            res.append(i)
            break
        elif x[0] == '3' and x[-1] == '0':
            res.append(i)
            break
        elif x[0] == '3' and x[-1] == '5' and x[1] == '0':
            res.append(i)
            break
        elif x[0] == '3' and x[1] == '5' and x[-2] == '0':
            res.append(i)
            break
        elif x[0] == '3' and x[1] == '5' and x[-2] == '0' and x[2] == '5':
            res.append(i)
            break
        elif x[0] == '5' and x[-1] == '0':
            res.append(i)
            break
        elif x[0] == '5' and x[-1] == '5' and x[1] == '0':
            res.append(i)
            break
        elif x[0] == '5' and x[1] == '5' and x[-2] == '0':
            res.append(i)
            break
        elif x[0] == '5' and x[1] == '5' and x[-2] == '0' and x[2] == '5':
            res.append(i)
            break
        elif x[0] == '7' and x[-1] == '0':
            res.append(i)
            break
        elif x[0] == '7' and x[-1] == '5' and x[1] == '0':
            res.append(i)
            break
        elif x[0] == '7' and x[1] == '5' and x[-2] == '0':
            res.append(i)
            break
        elif x[0] == '7' and x[1] == '5' and x[-2] == '0' and x[2] == '5':
            res.append(i)
            break
        elif x[0] == '8' and x[-1] == '0':
            res.append(i)
            break
        elif x[0] == '8' and x[-1] == '5' and x[1] == '0':
            res.append(i)
            break
        elif x[0] == '8' and x[1] == '5' and x[-2] == '0':
            res.append(i)
            break
        elif x[0] == '8' and x[1] == '5' and x[-2] == '0' and x[2] == '5':
            res.append(i)
            break
        elif x[0] == '9' and x[-1] == '0':
            res.append(i)
            break
        elif x[0] == '9' and x[-1] == '5' and x[1] == '0':
            res.append(i)
            break
        elif x[0] == '9' and x[1] == '5' and x[-2] == '0':
            res.append(i)
            break
        elif x[0] == '9' and x[1] == '5' and x[-2] == '0' and x[2] == '5':
            res.append(i)
            break
        elif x[0] == '0' and x[-1] == '5':
            res.append(i)
            break
        elif x[0] == '0' and x[-1] == '0':
            res.append(i)
            break
        elif x[0] == '0' and x[-1] == '5' and x[1] == '0':
            res.append(i)
            break
        elif x[0] == '0' and x[1] == '5' and x[-2] == '0':
            res.append(i)
            break
        elif x[0] == '0' and x[1] == '5' and x[-2] == '0' and x[2] == '5':
            res.append(i)
            break
        elif x[0] == '1' and x[-1] == '0':
            res.append(i)
            break
        elif x[0] == '1' and x[-1] == '5' and x[1] == '0':
            res.append(i
	