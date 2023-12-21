
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the given string
    palindromes = []
    for i in range(28, 95):
        for j in range(i+37, i+50):
            if string[i:j] == string[i:j][::-1]:
                palindromes.append(string[i:j])
    return set(palindromes)
