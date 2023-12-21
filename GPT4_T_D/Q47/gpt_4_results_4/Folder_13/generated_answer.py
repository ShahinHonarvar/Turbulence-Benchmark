
def palindromes_of_specific_lengths(s):
    substr = s[13:96]
    palindromes = set()
    for length in range(57, 61):
        for i in range(len(substr) - length + 1):
            candidate = substr[i:i+length]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate.lower())
    return palindromes
