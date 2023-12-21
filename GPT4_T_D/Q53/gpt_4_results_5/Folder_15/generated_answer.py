
def palindrome_of_length_at_least_n(s):
    s = s.lower()
    potential_palindromes = set()
    for i in range(len(s)):
        for j in range(i+4, len(s)+1):
            sub = s[i:j]
            if sub == sub[::-1]:
                if sub.isalpha():
                    potential_palindromes.add(sub)
    return potential_palindromes
