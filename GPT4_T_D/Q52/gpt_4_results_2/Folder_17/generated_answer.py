
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    length = len(s)
    
    for i in range(length):
        for j in range(i + 289, length + 1):
            substring = s[i:j]
            if len(substring) == 289 and substring.upper() == substring[::-1].upper():
                palindromes.add(substring)
                
    return palindromes
