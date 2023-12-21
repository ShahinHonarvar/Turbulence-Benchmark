
def all_left_right_truncatable_prime(test_list):
    res = []
    for a in test_list:
        l = str(a)
        cnt = 0
        while l:
            if l[0] == '0':
                break
            elif cnt == 0:
                l = l[1:]
            elif cnt == 1:
                l = l[:-1]
            cnt += 1
        if l == '0':
            break
        elif l in ['1', '2', '3', '5', '7', '11', '13', '17', '19']:
            res.append(a)
    return res
