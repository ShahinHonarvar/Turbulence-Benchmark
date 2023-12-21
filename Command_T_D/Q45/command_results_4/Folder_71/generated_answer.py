def palindromes_between_indices(s):
    try:
        return set(x[::-1] for x in [y for y in [z for z in s[i:j + 1]] if z.lower() in s[i:j + 1].lower()])
    except:
        return set()
