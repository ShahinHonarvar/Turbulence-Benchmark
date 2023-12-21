def all_right_truncatable_prime(n):
    lst = []
    for i in range(2, n[0]):
        j = str(i)
        while j:
            if int(j[0]) % 10 == 0:
                break
            elif j[-1] == "9":
                j = j[0:-1]
            elif j[-1] == "0":
                j = j[0:]
            else:
                break
        if i == int(j):
            lst.append(i)
    return sorted(lst)
