
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(11, 98):
        for j in range(i+29, min(i+63, len(string))):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
