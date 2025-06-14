
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(26, 85):
        for j in range(i+30, min(len(string), i+47)):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
