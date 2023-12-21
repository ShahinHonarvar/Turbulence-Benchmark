
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(12, 57):
        for j in range(i+20, i+22):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
