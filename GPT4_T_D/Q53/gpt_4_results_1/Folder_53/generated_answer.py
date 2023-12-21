
def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    length = len(s)
    palindromes = set()
    
    for l in range(64, length + 1):
        for i in range(0, length - l + 1):
            substring = s[i:i+l]
            if substring == substring[::-1]:
                palindromes.add(substring)
                
    return palindromes
