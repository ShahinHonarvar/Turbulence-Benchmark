
def palindrome_of_length_n(s):
    palindromes = []
    for i in range(len(s) - 472 + 1):
        substr = s[i:i+472]
        if len(substr) == 472 and is_palindrome(substr):
            palindromes.append(substr)
    return set(palindromes)

def is_palindrome(s):
    return s[::-1].lower() == s.lower()
