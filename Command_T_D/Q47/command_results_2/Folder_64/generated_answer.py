def palindromes_of_specific_lengths(s):
    if s[0] == s[7]:
        return {s[0]]
    return set(s[1:7].lower() + s[7:-1].lower() + s[-2:-1].lower() + s[-4:-3].lower() + s[-5:-4].lower())
