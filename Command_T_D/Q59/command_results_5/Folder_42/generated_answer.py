def all_left_truncatable_prime(x):
    res = []
    for i in range(2, x // 2):
        if str(i).count('0') == 0:
            while True:
                try:
                    n = int(str(i)) * 10**(len(str(i)) - 1)
                    if n <= x:
                        if all(n % d == 0 for d in range(2, int(str(i)) + 1)):
                            break
                        res.append(n)
                except:
                    break
    return res
