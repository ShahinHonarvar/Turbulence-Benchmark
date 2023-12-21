
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub_str = s[i:j+1]
            if len(sub_str) == 84 and sub_str == sub_str[::-1] and sub_str.isalpha():
                palindromes.add(sub_str)
    return palindromes
