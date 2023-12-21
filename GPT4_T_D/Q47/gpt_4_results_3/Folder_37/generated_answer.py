
def palindromes_of_specific_lengths(s):
    s = s[0:10].lower()
    palindromes = set()
    for i in range(3, 6):
        for j in range(len(s)-i+1):
            substring = s[j:j+i]
            if substring == substring[::-1] and substring.isalpha():
               palindromes.add(substring)
    return palindromes
