
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(26, 91):
        for j in range(i+27, min(len(string), i+59)):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
