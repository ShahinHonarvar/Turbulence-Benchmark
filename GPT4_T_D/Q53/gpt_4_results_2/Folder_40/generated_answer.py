
def palindrome_of_length_at_least_n(s):
    s = ''.join(ch for ch in s if ch.isalpha()).lower()
    palindromes = set()
    for length in range(3, len(s) + 1):
        for i in range(len(s) - length + 1):
            word = s[i:i + length]
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes
