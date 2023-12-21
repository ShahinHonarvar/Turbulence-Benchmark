def all_right_truncatable_prime(n):
    return sorted(
        filter(
            lambda p: p != "0"
            and p[0] != "9"
            and not (p[-1] == "0" and p[0] == "9")
            and str(p)[-1] in str(p)
            and all(
                int(str(p)[:i]) % int(str(p)[i]) == 0
                for i in range(1, len(str(p)) + 1)
            ),
            range(2, n[0] + 1),
        ),
        reverse=True,
    )
