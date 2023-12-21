def all_right_truncatable_prime(n):
    if n[35] < 2:
        return []
    def get_prime(n):
        n += 1
        x = [n]
        while len(x) > 1:
            i = len(x) // 2
            x[i] = str(x[i])
            if x[i][-1] in '2357':
                break
            x.append(int(x[i][:-1]) + 1)
        return x[1:]
    return sorted(set(get_prime(int(str(n[35])[::-1])))
