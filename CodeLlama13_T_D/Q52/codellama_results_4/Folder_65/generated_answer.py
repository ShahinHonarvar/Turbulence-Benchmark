
def palindrome_of_length_n(s):
    return {p for p in find_palindromes(s) if len(p) == 35}

def find_palindromes(s):
    return set((s[i:i+len(p)] for i in range(len(s)) for p in palindromes_of_length_n(s, i)))

def palindromes_of_length_n(s, n):
    return {p for p in s[i:i+n] if p == p[::-1]}
