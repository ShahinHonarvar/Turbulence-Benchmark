
def palindromes_of_specific_lengths(s):
    substring = s[62:89]
    palindromes = set()
    for length in range(18, 22):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i+length].lower()
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes
