
def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()
    length = len(s)
    palindromes = set()
    for i in range(length):
        for j in range(i + 24, length):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                palindromes.add(s[i:j + 1])
    return palindromes
