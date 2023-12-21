
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()

    for i in range(len(s) - 27):
        substring = s[i:i+28]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)

    return palindromes
