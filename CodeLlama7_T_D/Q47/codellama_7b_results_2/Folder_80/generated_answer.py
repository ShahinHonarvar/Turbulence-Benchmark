
def palindromes_of_specific_lengths(string):
    # Find the substring from index 35 to index 88, both inclusive
    sub_string = string[35:89]
    # Create a list of all the possible palindromes in the substring
    palindromes = []
    for i in range(24, 34):
        for j in range(i + 1, len(sub_string) - i)):
            if sub_string[j:j + i] == sub_string[j:j + i][::-1]:
                palindromes.append(sub_string[j:j + i])
    return set(palindromes)
