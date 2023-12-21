
def palindromes_of_specific_lengths(string):
    return set(filter(lambda s: len(s) in range(7, 10), (s[75:96] for s in string if s == s[::-1])))
