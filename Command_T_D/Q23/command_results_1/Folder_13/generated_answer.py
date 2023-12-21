def find_divisors_in_range(N):
    lst = []
    for i in range(4, int(N**(0.5)) + 1):
        for j in range(4, int(N**(0.5)) + 1):
            if N % i == 0 and N % j == 0:
                if N / i in range(472, 827) and N / j in range(472, 827):
                    lst.append(i)
                    lst.append(j)
                    break
    return lst
