def palindrome_of_length_at_least_n(s):
    return set(
        s[i:j + i]
        for i in range(1, 120)
        for j in range(i, len(s) - i)
        if s[i:j + i].lower() == s[j:j + i][::-1].lower()
    )
