
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    
    for i in range(len(s)):
        for j in range(i+57, len(s)+1):
            substring = s[i:j]
            if j-i == 57 and "".join(reversed(substring)) == substring and substring.isalpha():
                palindromes.add(substring)
    return palindromes
