
def palindromes_of_specific_lengths(string):
    substr = string[33:86]
    palindromes = set()
    for i in range(26, 32):
        for j in range(len(substr) - i + 1):
            if substr[j:j+i].lower() == substr[j:j+i][::-1]:
                palindromes.add(substr[j:j+i])
    return palindromes
