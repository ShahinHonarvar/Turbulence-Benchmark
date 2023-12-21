def palindromes_of_specific_lengths(s):
    return set(map(str.lower, s[1:-1:2] + s[2:-1:2] + s[3:-1:2] + s[4:-1:2] + s[5:-1:2] + s[6:-1:2] + s[7:-1:2]))
