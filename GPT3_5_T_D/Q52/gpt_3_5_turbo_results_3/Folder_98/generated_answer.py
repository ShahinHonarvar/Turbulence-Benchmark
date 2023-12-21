
def palindrome_of_length_n(s):
    n = 6
    s = s.lower()
    palindromes = set()
    
    for i in range(len(s)-n+1):
        substring = s[i:i+n]
        reversed_substring = substring[::-1]
        if substring.isalpha() and substring == reversed_substring:
            palindromes.add(substring)
    
    return palindromes
