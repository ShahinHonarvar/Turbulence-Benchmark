
def palindrome_of_length_at_least_n(s):
    s = ''.join([i.lower() if i.isalpha() else '' for i in s])  
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 93, len(s) + 1):
            sub_str = s[i:j]
            if sub_str == sub_str[::-1]:
                palindromes.add(sub_str)
    return palindromes
