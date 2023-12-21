
def palindromes_of_specific_lengths(string):
    # Find all palindromes with lengths between 4 and 5, both inclusive
    palindromes = []
    for i in range(10, 89):
        for j in range(i+3, i+6):
            if string[i:j] == string[i:j][::-1]:
                palindromes.append(string[i:j])
    
    # Return the set of all palindromes with lengths between 4 and 5, both inclusive
    return set(palindromes)
