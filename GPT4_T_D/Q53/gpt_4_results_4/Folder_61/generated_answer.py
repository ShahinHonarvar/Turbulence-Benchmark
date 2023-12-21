
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 5, len(s)+1):
            substring = s[i:j]
            if substring == substring[::-1] and set(substring).issubset(valid_chars):
                palindromes.add(substring)
    return palindromes
