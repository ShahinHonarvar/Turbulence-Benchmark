
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(11, 98):
        for j in range(i+28, min(len(string), i+63)):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
