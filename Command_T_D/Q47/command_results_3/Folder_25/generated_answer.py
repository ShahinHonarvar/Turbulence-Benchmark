def palindromes_of_specific_lengths(s):
    return {p for i in range(26, 84) for j in range(30, 46) for p in s[i:-i][::-1].lower() if p in p}
