
def palindromes_of_specific_lengths(s):
    import re
    s = s[31:75]
    length = len(s)
    result = set()
    for length_palindrome in range(23, 40):
        for start in range(length - length_palindrome + 1):
            candidate = s[start:start + length_palindrome]
            if candidate.lower() == candidate.lower()[::-1] and re.search(a-z, candidate.lower()) is not None:
                result.add(candidate.lower())
    return result
