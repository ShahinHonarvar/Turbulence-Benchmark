def palindromes_between_indices(s):
    letters = set(s.lower()[:5])
    return set(f'{s[0]}{s[1]}{s[2]}{s[3]}{s[4]}{s[0][::-1]}{s[1][::-1]}{s[2][::-1]}{s[3][::-1]}{s[4][::-1]}')
