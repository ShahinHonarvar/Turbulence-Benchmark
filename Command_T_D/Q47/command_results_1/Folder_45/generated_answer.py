def palindromes_of_specific_lengths(s):
    return {x[70:140] for x in s.lower() if x[70:140] in s[70:140] and len(x) in range(3, 61)}
