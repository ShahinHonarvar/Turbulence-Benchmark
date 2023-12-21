
def palindrome_of_length_n(s):
    s = s.lower()
    len_s = len(s)
    palindromes = set()
    
    for i in range(len_s):
        for j in range(i + 63, min(i + 127, len_s) + 1, 2):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes
