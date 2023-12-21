def palindromes_of_specific_lengths(s):
    return set(
        s[i:i + 20].lower()
        for i in range(15, 95) if i > 0 and s[i - 1] == s[i + 19] and s[i - 1] in 'qwertyuiopasdfghjklzxcvbnm'
    )
