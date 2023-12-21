
def palindromes_of_specific_lengths(s):
    s = s[:31]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+20, i+31):
            substring = s[i:j]
            reversed_substring = substring[::-1]
            if substring == reversed_substring and substring.isalpha():
                palindromes.add(substring.lower())
    return palindromes
