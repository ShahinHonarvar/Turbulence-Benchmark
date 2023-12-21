
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(13, 96):
        for j in range(i+57, min(i+60, len(string))):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
