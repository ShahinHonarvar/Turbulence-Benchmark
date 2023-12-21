
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(40, 95):
        for j in range(i+1, min(len(string), i+52)):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
