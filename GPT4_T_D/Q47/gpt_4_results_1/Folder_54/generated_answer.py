
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[27:78]
    for i in range(len(substring)):
        for j in range(i+18, min(i+20, len(substring)+1)):
            candidate = substring[i:j]
            if candidate == candidate[::-1] and candidate.isalpha():
                palindromes.add(candidate.lower())
    return palindromes
