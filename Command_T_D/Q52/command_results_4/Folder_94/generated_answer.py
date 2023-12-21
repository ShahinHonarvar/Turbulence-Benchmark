def palindrome_of_length_n(s):
    return set(
        [s[i:j + 1] for i in range(len(s) - 1) for j in range(i, -1, -1) if s[i:j + 1] == s[j:i + 1]]
    )
