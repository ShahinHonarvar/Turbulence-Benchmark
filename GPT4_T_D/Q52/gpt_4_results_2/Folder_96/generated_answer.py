
def palindrome_of_length_n(s):
    s = s.lower()
    length = 83
    palindromes = set()

    for i in range(len(s)):
        for j in range(i+length, len(s)+1):
            sub = s[i:j]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub)

    return palindromes
