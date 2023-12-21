def palindromes_between_indices(s):
    return set(f'{s[3:9]}{s[3:9][::-1]}')
