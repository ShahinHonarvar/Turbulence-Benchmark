def all_right_truncatable_prime(x):
    l = []
    for n in range(x - 1, 1, -1):
        if n % 2 == 0 or n % 5 == 0 or n % 3 == 0:
            continue
        for i in range(1, int(str(n)[-1]) + 1):
            if str(n)[-i:] == str(n)[-1]:
                break
            elif int(str(n)[-i:]) == int(str(n)[-1]):
                l.append(n)
                break
    return l
