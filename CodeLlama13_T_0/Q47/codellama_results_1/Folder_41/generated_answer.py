
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(1, 7):
        for j in range(i+2, min(len(string), i+5)):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
