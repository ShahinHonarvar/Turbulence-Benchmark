
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    i, length = 0, len(s)
    palindromes = set()
    
    while i < length:
        for end in range(length, i+52, -1):
            if s[i : end] == s[i : end][::-1] and s[i:end].isalpha():
                palindromes.add(s[i : end])
        i += 1
    return palindromes
