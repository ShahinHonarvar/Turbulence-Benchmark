def palindromes_between_indices(s):
    indices = range(0, len(s) + 1)
    letters = set(s[0:7])
    return {i * i for i in indices if i in letters and s[i:i+i].lower() == s[i:i+i][::-1].lower() }
