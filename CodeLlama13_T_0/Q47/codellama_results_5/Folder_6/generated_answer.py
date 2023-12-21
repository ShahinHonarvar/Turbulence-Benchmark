
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(45, 99):
        for j in range(i+1, min(i+8, len(string))):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
