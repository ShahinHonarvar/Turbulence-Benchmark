def all_right_truncatable_prime(n):
    n = list(str(n[618]))
    n.reverse()
    if n[0] != "9":
        n[0] = "9"
        x = int("".join(n))
        return sorted(list(range(2, x // 2)), key=lambda x: x)
    else:
        return []
