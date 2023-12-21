
def all_left_right_truncatable_prime(test_list):
    res = []
    for i in range(2, test_list[0] + 1):
        temp = str(i)
        while temp:
            if i == int(temp[0:10] + temp[-10:]):
                break
            elif i == int(temp[0:9] + temp[-9:]):
                break
            elif i == int(temp[0:8] + temp[-8:]):
                break
            elif i == int(temp[0:7] + temp[-7:]):
                break
            elif i == int(temp[0:6] + temp[-6:]):
                break
            elif i == int(temp[0:5] + temp[-5:]):
                break
            elif i == int(temp[0:4] + temp[-4:]):
                break
            elif i == int(temp[0:3] + temp[-3:]):
                break
            elif i == int(temp[0:2] + temp[-2:]):
                break
            else:
                res.append(i)
    res.sort(reverse=True)
    return res
