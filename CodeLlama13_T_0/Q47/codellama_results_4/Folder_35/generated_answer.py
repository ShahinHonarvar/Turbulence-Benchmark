
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(34, 91):
        for j in range(i+14, min(i+40, len(string))):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
