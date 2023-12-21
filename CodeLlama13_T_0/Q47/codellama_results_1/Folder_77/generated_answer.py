
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(103, 276+1):
        for j in range(i+99, min(len(string), i+169)+1):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
