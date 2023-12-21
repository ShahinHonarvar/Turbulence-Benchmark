
def palindromes_of_specific_lengths(s):
    s = s[124:284]
    palindromes = set()
    for i in range(150):
        for j in range(i + 115, i + 135):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes
