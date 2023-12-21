
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    set_of_palindromes = set()
    
    for i in range(len(s)):
        for j in range(i + 32, len(s) + 1):
            if s[i:j] == s[i:j][::-1] and s[i:j].isalpha():
                set_of_palindromes.add(s[i:j])
    
    return set_of_palindromes
