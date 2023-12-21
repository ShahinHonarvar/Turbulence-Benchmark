
def palindrome_of_length_n(s: str):
    s = s.lower()
    length = 7
    palindromes = set()

    for i in range(len(s)):
        if i + length > len(s):
            break
        substring = s[i:i+length]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)

    return palindromes
