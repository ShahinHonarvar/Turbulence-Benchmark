
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(0, 301):
        for j in range(i+50, min(i+61, len(string))):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
