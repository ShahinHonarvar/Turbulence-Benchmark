
def palindromes_of_specific_lengths(s):
    s = s.lower()
    substring = s[44:100]
    palindromes = set()

    for start in range(len(substring)):
        for length in range(13, 43):
            if start + length > len(substring):
                break

            candidate = substring[start:start + length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)

    return palindromes
