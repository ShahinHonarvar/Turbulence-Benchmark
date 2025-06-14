
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(24, 85):
        for j in range(i+1, min(len(string), 85)):
            substr = string[i:j]
            if len(substr) >= 21 and len(substr) <= 31 and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
