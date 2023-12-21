
def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i+25, len(s)+1):
            potential_palindrome = s[i:j]
            if potential_palindrome == potential_palindrome[::-1] and all(c.isalpha() for c in potential_palindrome):
                palindromes.add(potential_palindrome)
    return palindromes
