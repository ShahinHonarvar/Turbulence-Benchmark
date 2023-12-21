
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(15, 87):
        for j in range(i+50, min(len(string), i+61)):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
