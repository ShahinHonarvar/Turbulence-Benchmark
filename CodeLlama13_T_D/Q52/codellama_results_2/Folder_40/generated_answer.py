
def palindrome_of_length_n(s):
    return {p for p in find_palindromes(s) if len(p) == 3}

def find_palindromes(s):
    return (p for p in s.lower() if p[::-1] == p)
