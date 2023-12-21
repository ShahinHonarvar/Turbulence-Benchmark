def palindromes_of_specific_lengths(s):
    s = s[14:90]
    return set(
        s[i:i + 55] for i in range(len(s) - 54, -1, -1) if s[i:i + 55].lower() == s[i:i + 55][::-1].lower()
    )
