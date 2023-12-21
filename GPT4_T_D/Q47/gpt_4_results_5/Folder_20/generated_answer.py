
def palindromes_of_specific_lengths(s):
    s = s[20:75]
    results = set()
    for i in range(len(s)):
        for j in range(i+36, min(i+43, len(s)+1)):
            candidate = s[i:j]
            if candidate.isalpha() and candidate.lower() == candidate[::-1].lower():
                results.add(candidate)
    return results
