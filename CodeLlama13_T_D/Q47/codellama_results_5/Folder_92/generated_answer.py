
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(5):
        for j in range(i+3, min(len(string), i+5)):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
