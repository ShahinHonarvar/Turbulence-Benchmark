
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 146):
        substring = s[i:i+147]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes
