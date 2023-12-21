
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 78, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                if all(97 <= ord(char) <= 122 for char in substring): 
                    palindromes.add(substring)
    return palindromes
