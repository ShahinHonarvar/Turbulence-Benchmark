
def all_left_right_truncatable_prime(test_n):
    res = []
    for n in range(2, test_n[0] + 1):
        c = 10**(len(str(n)) - 1)
        while True:
            if c <= test_n[1] and n % c == 0:
                break
            elif c == 1:
                if n % 10 == 0:
                    break
                else:
                    res.append(n)
                    break
            elif c == 2:
                if n % 5 == 0:
                    break
                else:
                    res.append(n)
                    break
            elif c == 3:
                if n % 5 == 0 or n % 10 == 0:
                    break
                else:
                    res.append(n)
                    break
            elif c == 4:
                if n % 2 == 0 or n % 5 == 0 or n % 10 == 0:
                    break
                else:
                    res.append(n)
                    break
            elif c == 5:
                if n % 2 == 0 or n % 5 == 0 or n % 10 == 0 or n % 15 == 0:
                    break
                else:
                    res.append(n)
                    break
            elif c == 6:
                if n % 2 == 0 or n % 5 == 0 or n % 10 == 0 or n % 15 == 0 or n % 21 == 0:
                    break
                else:
                    res.append(n)
                    break
            elif c == 7:
                if n % 2 == 0 or n % 5 == 0 or n % 10 == 0 or n % 15 == 0 or n % 21 == 0 or n % 35 == 0:
                    break
                else:
                    res.append(n)
                    break
            elif c == 8:
                if n % 2 == 0 or n % 5 == 0 or n % 10 == 0 or n % 15 == 0 or n % 21 == 0 or n % 35 == 0 or n % 42 == 0:
                    break
                else:
                    res.append(n)
                    break
            elif c == 9:
                if n % 2 == 0 or n % 5 == 0 or n % 10 == 0 or n % 15 == 0 or n % 21 == 0 or n % 35 == 0 or n % 42 == 0 or n % 63 == 0:
                    break
                else:
                    res.append(n)
                    break
            c += 1
    return res
