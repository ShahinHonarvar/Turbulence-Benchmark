
def palindrome_of_length_n(s):
    s = s.lower()
    s = ''.join(x for x in s if x.isalpha())
    
    palindromes = set()
    for i in range(len(s)-98):
        substring = s[i:i+99]
        if substring == substring[::-1]:
            palindromes.add(substring)
            
    return palindromes
