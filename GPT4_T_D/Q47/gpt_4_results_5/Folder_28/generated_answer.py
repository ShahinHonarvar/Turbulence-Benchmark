
def palindromes_of_specific_lengths(string):
    import re
    substring = string[32:72]
    palindrome_set = set()
    for length in range(21, 33):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start+length]
            if candidate == candidate[::-1] and re.match('^[a-zA-Z]*$', candidate):
                palindrome_set.add(candidate.lower())
    return palindrome_set
