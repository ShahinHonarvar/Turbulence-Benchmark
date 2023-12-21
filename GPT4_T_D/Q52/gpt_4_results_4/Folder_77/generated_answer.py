
def palindrome_of_length_n(s):
    s = s.lower()
    s = "".join(ch for ch in s if ch.isalpha())
    length = 173
    palindromes = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i+length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
