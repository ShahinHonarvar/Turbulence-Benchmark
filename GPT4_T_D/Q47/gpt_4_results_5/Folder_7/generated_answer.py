
def palindromes_of_specific_lengths(s):
    s = s[119:257]
    palindromes = set()
    for l in range(104, 124):
        for i in range(0, len(s)-l+1):
            substring = s[i:i+l]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring)
    return palindromes
