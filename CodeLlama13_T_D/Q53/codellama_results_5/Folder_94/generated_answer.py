
def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(41, len(s) + 1):
        for j in range(len(s) - i + 1):
            if s[j:j+i] == s[j+i-1::-1]:
                palindromes.add(s[j:j+i])
    return palindromes
