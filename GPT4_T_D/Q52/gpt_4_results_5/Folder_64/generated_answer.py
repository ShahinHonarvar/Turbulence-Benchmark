
def palindrome_of_length_n(s):
    s = s.lower()
    substrings = {s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if len(s[i:j]) == 9}
    palindromes = set()
    
    for substr in substrings:
        if substr.isalpha() and substr == substr[::-1]:
            palindromes.add(substr)
    
    return palindromes
