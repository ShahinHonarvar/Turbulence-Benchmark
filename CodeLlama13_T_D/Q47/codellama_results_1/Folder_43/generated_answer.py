
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(41, 90):
        for j in range(i + 22, min(len(string), i + 38)):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
