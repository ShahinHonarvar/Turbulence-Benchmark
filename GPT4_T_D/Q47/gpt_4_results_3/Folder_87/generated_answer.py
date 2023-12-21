
def palindromes_of_specific_lengths(string):
    string = string[11:94].lower()
    palindromes = set()
    for length in range(34, 55):
        for i in range(len(string) - length + 1):
            subset = string[i:i+length]
            if subset == subset[::-1] and subset.isalpha():
                palindromes.add(subset)
    return palindromes
