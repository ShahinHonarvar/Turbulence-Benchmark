
def palindrome_of_length_at_least_n(s):
    s = ''.join(ch for ch in s if ch.isalpha()).lower()
    length = len(s)
    palindromes = set()
    for idx in range(length):
        for end in range(idx + 24, length + 1):
            if s[idx:end] == s[idx:end][::-1]:
                palindromes.add(s[idx:end])
    return palindromes
