
def palindrome_of_length_at_least_n(s):
    s = "".join(ch for ch in s if ch.isalpha()).lower()
    n = 115
    palindromes = set()
    
    for size in range(n, len(s) + 1):
        for start in range(0, len(s) - size + 1):
            substring = s[start:start + size]
            if substring == substring[::-1]:
                palindromes.add(substring)
            
    return palindromes
