
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(13, 100):
        for j in range(i+26, i+30):
            substr = string[i:j]
            if len(substr) % 2 == 0 and substr[::-1].lower() == substr.lower():
                palindromes.add(substr)
    return palindromes
