
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the given string
    palindromes = []
    for i in range(130, 296):
        for j in range(i+103, i+159):
            if string[i:j] == string[i:j][::-1]:
                palindromes.append(string[i:j])
    return set(palindromes)
