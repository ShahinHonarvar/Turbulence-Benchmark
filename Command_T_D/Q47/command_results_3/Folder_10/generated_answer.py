def palindromes_of_specific_lengths(s):
    return set(
        l
        for l in range(16, 40)
        if l * 2 - 1 <= len(s) - 16
        and s[16:l] == s[l:-l]
        and all(c.lower() in 'qwertyuiopasdfghjklzxcvbnm' for c in s[16:l])
    )
