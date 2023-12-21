
def palindrome_of_length_n(s):
    s = s.lower()
    length = 59
    palindromes = set()

    for i in range(len(s)):
        for j in range(i+length, len(s)+1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    
    return palindromes
