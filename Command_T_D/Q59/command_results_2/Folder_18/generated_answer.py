def all_left_truncatable_prime(x_list):
    x = x_list[429]
    lst = []
    for x in range(x // 10, x, -1):
        if x * 10 <= x:
            for i in range(1, x // 10 + 1):
                if all(a % 10 == b for a, b in zip(str(x), str(x - i))):
                    lst.append(x - i)
                    break
    return sorted(lst)
