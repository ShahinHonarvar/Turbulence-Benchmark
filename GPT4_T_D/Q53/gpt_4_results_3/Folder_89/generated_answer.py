
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    set_of_palindromes = set()
    for i in range(len(s)):
        for j in range(i + 43, len(s)+1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                set_of_palindromes.add(substring)
    return set_of_palindromes
