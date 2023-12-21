
def all_left_right_truncatable_prime(test_list):
    res = []
    for a in test_list:
        if a == 1:
            break
        for b in range(2, int(str(a)[0]) + 1):
            if b == 1:
                break
            c = int(str(a)[-1])
            d = int(str(a)[0])
            for k in range(1, c + 1):
                if a % 10**(k - 1) == 0:
                    break
                a = a // 10**(k - 1)
            if a == 1:
                break
            for l in range(2, d + 1):
                if a % 10**(c - l - 1) == 0:
                    break
                a = a // 10**(c - l - 1)
            if a == 1:
                break
            if all(str(a)[i] == '9' for i in range(1, len(str(a)))):
                break
            if isprime(a):
                res.append(a)
    return res
