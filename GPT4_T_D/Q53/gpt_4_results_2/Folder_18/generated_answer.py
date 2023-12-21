
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 62, len(s) + 1):
            sub_str = s[i:j]
            if sub_str == sub_str[::-1] and sub_str.isalpha():
                palindromes.add(sub_str)
    return palindromes
