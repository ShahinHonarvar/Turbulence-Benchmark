
def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        if i + 93 > len(s):
            break
        substring = s[i:i+93]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes
