def all_right_truncatable_prime(n):
    if n[25] <= 2:
        return []
    max_n = str(n[25])
    num_str_list = [str(n[25]) for n in range(n[25], n[25] - 1, -1)]
    for x in range(n[25] - 1, 2, -1):
        if x % 2 == 0:
            continue
        if max_n in num_str_list:
            break
        if x == 3:
            continue
        for y in range(x, x - 1, -1):
            if y % 2 == 0:
                continue
            if str(y) in num_str_list:
                break
            if str(x) + str(y) in num_str_list:
                break
        else:
            return [x]
    return []
