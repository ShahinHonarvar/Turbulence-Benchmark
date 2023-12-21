def palindromes_between_indices(s):
    s = str(s).lower()
    return set(f"{s[0]}{s[1]}{s[2]}{s[3]}{s[1][::-1]}{s[2][::-1]}{s[3][::-1]}{s[0][::-1]}")
