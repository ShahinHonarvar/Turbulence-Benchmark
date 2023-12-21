
def palindromes_of_specific_lengths(s):
    s1 = s[43:96].lower()
    palindromes = set()
    for i in range(len(s1)):
        for j in range(i+18, min(i+48, len(s1)+1)):
            substring = s1[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
