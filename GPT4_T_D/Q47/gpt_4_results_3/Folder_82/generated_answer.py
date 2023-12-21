
def palindromes_of_specific_lengths(s):
    s = s[3:301]

    palindromes = set()

    for length in range(30, 301):
        for start in range(len(s) - length + 1):
            substring = s[start: start + length]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    
    return palindromes
