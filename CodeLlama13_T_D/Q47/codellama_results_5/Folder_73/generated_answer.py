
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(21, 63):
        for j in range(i+1, min(len(string), 64)):
            substr = string[i:j]
            if len(substr) >= 22 and len(substr) <= 33:
                if substr == substr[::-1]:
                    palindromes.add(substr)
    return palindromes
