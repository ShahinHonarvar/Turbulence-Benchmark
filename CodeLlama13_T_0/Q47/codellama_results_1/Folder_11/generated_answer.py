
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(24, 98):
        for j in range(i+10, min(i+37, len(string))):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
