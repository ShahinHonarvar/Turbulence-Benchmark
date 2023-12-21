def palindromes_of_specific_lengths(s):
    return {p for p in s[11:-12:-1].split() if p.lower() == p[::-1].lower() and len(p) in range(13, 67)}
