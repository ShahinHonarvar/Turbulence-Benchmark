
def palindromes_of_specific_lengths(string):
    string = string[15:95].lower()

    palindromes = set()
    for length in range(18, 74):
        for i in range(len(string)):
            extract = string[i:i + length]
            if extract == extract[::-1] and extract.isalpha():
                palindromes.add(extract)
    return palindromes
