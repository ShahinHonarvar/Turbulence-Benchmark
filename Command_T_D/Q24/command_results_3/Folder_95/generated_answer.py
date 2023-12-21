def sum_of_divisors_in_range(N):
    divs = []
    if N >= 35:
        for d in range(N // 2, N // 3, 2):
            if d == N // 2 or d == N // 3:
                continue
            elif d not in divs:
                divs.append(d)
        for d in range(N // 3, N // 5, 3):
            if d == N // 3 or d == N // 5:
                continue
            elif d not in divs:
                divs.append(d)
        for d in range(N // 5, N // 7, 5):
            if d == N // 5 or d == N // 7:
                continue
            elif d not in divs:
                divs.append(d)
        for d in range(N // 7, N // 9, 7):
            if d == N // 7 or d == N // 9:
                continue
            elif d not in divs:
                divs.append(d)
    return sum(divs) if len(divs) > 0 else 0
