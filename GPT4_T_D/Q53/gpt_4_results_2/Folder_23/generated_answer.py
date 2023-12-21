
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    potential_palindromes = set()
    for len_sub in range(19, len(s) + 1):
        for i in range(len(s) - len_sub + 1):
            substring = s[i:i+len_sub]
            if substring == substring[::-1] and substring.isalpha():
                potential_palindromes.add(substring)
    return potential_palindromes
