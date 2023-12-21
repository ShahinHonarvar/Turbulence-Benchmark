
def palindromes_of_specific_lengths(s):
    s = s[:21]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+5, min(i+81, len(s)+1)):
            substring = s[i:j]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                palindromes.add(substring)
    return palindromes
