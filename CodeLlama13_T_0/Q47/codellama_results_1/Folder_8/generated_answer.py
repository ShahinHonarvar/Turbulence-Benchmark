
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(17, 73):
        for j in range(i+50, i+52):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
