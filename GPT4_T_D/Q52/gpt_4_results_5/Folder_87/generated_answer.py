
def palindrome_of_length_n(s):
    import re
    s = re.sub(r'\W+', '', s).lower()
    n = 57
    s_len = len(s)
    palindromes = set()
    for i in range(s_len - n + 1):
        test_palindrome = s[i:i+n]
        if test_palindrome == test_palindrome[::-1]:
            palindromes.add(test_palindrome)
    return palindromes
