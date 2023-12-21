
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(28, 94+1):
        for j in range(i, min(len(string), i + 40)):
            substr = string[i:j]
            if len(substr) >= 38 and len(substr) <= 49 and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
