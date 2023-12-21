
def palindromes_between_indices(s):
    return { ''.join(reversed(substring)) for substring in all_substrings(s[2:7]) if is_palindrome(substring) }

def all_substrings(s):
    return [''.join(s[i:j+1]) for i in range(len(s)) for j in range(i, len(s))]

def is_palindrome(s):
    return s == ''.join(reversed(s))
