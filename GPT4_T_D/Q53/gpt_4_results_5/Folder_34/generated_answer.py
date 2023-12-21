
def palindrome_of_length_at_least_n(s):
    s = ''.join(ch for ch in s if ch.isalpha()).lower()
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i+67, length):
            if s[i:j+1] == s[i:j+1][::-1]:
                palindromes.add(s[i:j+1])
    return palindromes
