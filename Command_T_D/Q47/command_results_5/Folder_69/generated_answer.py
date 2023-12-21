def palindromes_of_specific_lengths(s):
    return {x[::-1] for x in s[11:-1:-1].split(" ")[11:-1:-1] if len(x) in range(45, 52)}
