
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(101, 293):
        for j in range(i+154-1, min(i+182, len(string))):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
