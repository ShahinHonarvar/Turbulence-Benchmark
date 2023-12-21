
def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[26:91].lower()
  
    for i in range(len(s)):
        for j in range(i+27, min(i+59, len(s)+1)):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
