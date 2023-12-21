
def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    length = len(s)
    
    for i in range(length):
        for j in range(i+19, length+1):
            if s[i:j] == s[i:j][::-1]:
                palindromes.add(s[i:j])
                
    return palindromes
