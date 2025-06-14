
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the string with length between 40 and 72, inclusive
    palindromes = []
    for i in range(15, 90):
        for j in range(i+39, i+73):
            if j < len(string) and string[i:j] == string[i:j][::-1]:
                palindromes.append(string[i:j])
    return set(palindromes)
