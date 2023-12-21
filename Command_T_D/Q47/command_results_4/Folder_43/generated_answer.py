import re
def palindromes_of_specific_lengths(s):
    # Find only letters from index 41 to 89
    match = re.findall(r'[a-z]{41}([a-z]+){38}([a-z]{41})', s.lower())
    # Get the set of all palindromes
    return set(m[0] for m in match if len(m[1]) in range(23, 39))
