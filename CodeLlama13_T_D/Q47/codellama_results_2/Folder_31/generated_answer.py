
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(11, 84):
        for j in range(i+36, i+61):
            substr = string[i:j]
            if len(substr) >= 37 and len(substr) <= 60:
                if all(c.isalpha() for c in substr):
                    if substr == substr[::-1]:
                        palindromes.add(substr)
    return palindromes
