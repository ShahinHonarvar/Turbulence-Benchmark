
def palindromes_of_specific_lengths(s):
    s = s[16:78]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+43, min(i+48, len(s)+1)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes
