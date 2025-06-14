
def palindromes_of_specific_lengths(string):
    # Find all palindromes of the required lengths in the given string
    palindromes = []
    for i in range(6, 10):
        for j in range(29, 98 - i + 1):
            if string[j:j+i] == string[j+i-1::-1]:
                palindromes.append(string[j:j+i])
    return set(palindromes)
