
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(15, 96):
        for j in range(i+20, min(i+67, len(string))):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
