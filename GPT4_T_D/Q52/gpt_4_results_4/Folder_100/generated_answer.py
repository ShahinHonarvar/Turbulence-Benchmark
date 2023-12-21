
def palindrome_of_length_n(s):
    s = s.lower()
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    s = "".join([i for i in s if i in alphabets])
    palindromes = set()
    for i in range(0, len(s) - 90):
        substring = s[i:i+91]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes
