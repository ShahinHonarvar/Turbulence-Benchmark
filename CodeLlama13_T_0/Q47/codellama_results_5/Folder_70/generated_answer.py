
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(10, 71):
        for j in range(i+24, min(len(string), i+53)):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
