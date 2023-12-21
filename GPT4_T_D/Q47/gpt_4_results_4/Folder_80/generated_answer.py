
def palindromes_of_specific_lengths(s):
    s = s[35:89]
    palindromes = set()

    for length in range(24, 34):
        for i in range(0, len(s) - length + 1):
            substring = s[i:i+length]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)

    return palindromes
