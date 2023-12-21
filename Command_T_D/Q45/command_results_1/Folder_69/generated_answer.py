def palindromes_between_indices(s):
    if len(s) < 4:
        return set()
    letters = set(s[0:4].lower())
    return {s[i:i+4] for i in range(0, len(s) - 3)} & {s[i:i+4][::-1] for i in range(0, len(s) - 3)} & {s[i:i+4] + s[i:i+4][::-1] for i in range(0, len(s) - 3)} & {s[i:i+4] + s[i:i+4][::-1] + s[i:i+4] for i in range(0, len(s) - 3)}
