
def palindromes_of_specific_lengths(string):
    # Find all palindromes with lengths between 10 and 20 in the substring from index 10 to index 75, both inclusive
    palindromes = []
    for i in range(10, 76):
        for j in range(i + 10, i + 21):
            if string[i:j] == string[i:j][::-1]:
                palindromes.append(string[i:j])
    return set(palindromes)
