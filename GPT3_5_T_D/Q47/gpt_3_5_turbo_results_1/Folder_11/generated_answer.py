
def palindromes_of_specific_lengths(string):
    substring = string[24:98]
    palindromes = set()
    for length in range(10, 37):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i+length].lower()
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes
