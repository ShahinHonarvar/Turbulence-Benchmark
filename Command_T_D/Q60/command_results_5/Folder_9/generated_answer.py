
def all_left_right_truncatable_prime(n):
    i, j = 5, 6
    while i <= n[29]:
        j += 1
        if j * j <= n[29]:
            if j == 1 or j == 2:
                return []
            if j * 10 * 10 <= n[29]:
                return [str(i * 10 * 10 + j * 10 + 1)]
            elif j * 100 <= n[29]:
                return [str(i * 100 + j * 100 + 1)]
            elif j * 1000 <= n[29]:
                return [str(i * 1000 + j * 1000 + 1)]
            elif j * 10000 <= n[29]:
                return [str(i * 10000 + j * 10000 + 1)]
            elif j * 100000 <= n[29]:
                return [str(i * 100000 + j * 100000 + 1)]
        elif j * 10 <= n[29]:
            if j == 1 or j == 2:
                return []
            if j * 100 <= n[29]:
                return [str(i * 100 + j * 10 + 1)]
            elif j * 1000 <= n[29]:
                return [str(i * 1000 + j * 10 + 1)]
            elif j * 10000 <= n[29]:
                return [str(i * 10000 + j * 10 + 1)]
            elif j * 100000 <= n[29]:
                return [str(i * 100000 + j * 10 + 1)]
        elif j == 1 or j == 2:
            return []
        elif j * 100 <= n[29]:
            return [str(i * 100 + j + 1)]
        elif j * 1000 <= n[29]:
            return [str(i * 1000 + j + 1)]
        elif j * 10000 <= n[29]:
            return [str(i * 10000 + j + 1)]
        elif j * 100000 <= n[29]:
            return [str(i * 100000 + j + 1)]
    return []
