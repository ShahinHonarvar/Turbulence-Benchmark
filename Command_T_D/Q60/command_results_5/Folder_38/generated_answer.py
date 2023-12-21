
def all_left_right_truncatable_prime(test_tup):
    res = []
    for primenum in range(2, int(test_tup[28]) + 1):
        cnt = 0
        while cnt < len(str(primenum)):
            if str(primenum)[cnt] == '0':
                break
            elif str(primenum)[cnt] == '1' or str(primenum)[cnt] == '2':
                cnt += 1
            else:
                break
        cnt -= 1
        while cnt >= 0:
            if str(primenum)[cnt] == '0':
                break
            elif str(primenum)[cnt] == '1' or str(primenum)[cnt] == '2':
                cnt += 1
            else:
                break
        if primenum > 1 and primenum < 10**2:
            res.append(primenum)
    return res
