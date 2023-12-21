
def palindromes_of_specific_lengths(string):
    substr = string[1:7]
    palindromes = set()
    for i in range(3, 5):
        for j in range(len(substr) - i + 1):
            if substr[j:j+i] == substr[j+i-1::-1]:
                palindromes.add(substr[j:j+i])
    return palindromes
