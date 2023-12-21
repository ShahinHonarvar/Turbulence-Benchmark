
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(10, 75+1):
        for j in range(i+9, i+20+1):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
