
def palindromes_of_specific_lengths(string):
    string = string[12:123]
    results = set()
    for length in range(12, 221):
        for start in range(len(string) - length + 1):
            candidate = string[start: start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                results.add(candidate.lower())
    return results
