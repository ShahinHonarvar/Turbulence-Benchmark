
def palindrome_of_length_at_least_n(string):
    import re
    pattern = re.compile(r'[a-zA-Z]+')
    
    palindromes = set()
    n = len(string)
    for i in range(n-139):
        for j in range(i+140, n+1):
            substr = string[i:j].lower()
            if substr == substr[::-1]:
                palindromes.add(substr)
    
    return palindromes
