
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 276, len(s) + 1):
            substr = s[i:j]
            if len(substr) == 276 and all(char.isalpha() for char in substr):
                if substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes
