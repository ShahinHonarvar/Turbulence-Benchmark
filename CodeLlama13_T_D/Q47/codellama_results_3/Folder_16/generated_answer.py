
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the given string with lengths between 51 and 60
    palindromes = []
    for i in range(len(string) - 60, len(string) - 51 + 1):
        for j in range(i + 60, i + 51 - 1, -1):
            if string[i:j] == string[i:j][::-1]:
                palindromes.append(string[i:j])
    return set(palindromes)
