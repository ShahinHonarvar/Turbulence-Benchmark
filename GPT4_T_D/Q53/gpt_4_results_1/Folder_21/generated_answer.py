
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 112, length + 1):
            sub = s[i:j]
            if sub == sub[::-1] and all(char.isalpha() for char in sub):
                palindromes.add(sub)
    return palindromes
