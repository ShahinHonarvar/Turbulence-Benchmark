
def palindromes_of_specific_lengths(s):
    s = s[33:86]
    palindromes = set()

    for length in range(26, 32):
        for i in range(len(s)):
            if i + length > len(s):
                break
            substring = s[i:i+length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())

    return palindromes
