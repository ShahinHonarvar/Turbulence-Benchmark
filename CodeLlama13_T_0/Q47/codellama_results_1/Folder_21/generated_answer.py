
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(100, 296):
        for j in range(i+135, i+161):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
