
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(23, 78):
        for j in range(i+13, min(len(string), i+40)):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
