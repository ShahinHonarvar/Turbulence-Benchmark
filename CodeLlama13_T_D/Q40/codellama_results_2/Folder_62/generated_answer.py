
def return_n_smallest_chars(s):
    return sorted([c for c in s if c not in 'aeiou'], reverse=True)[:84]
