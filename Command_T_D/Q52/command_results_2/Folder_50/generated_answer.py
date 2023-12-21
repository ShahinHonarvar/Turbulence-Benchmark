def palindrome_of_length_n(s):
    return set(
        "".join(
            s[i : j + 1]
            for i in range(len(s) - 40, -1, -1)
            for j in range(i, i + 40)
        ).lower()
        for i in range(len(s) - 40, -1, -1)
        for j in range(i, i + 40)
    )
