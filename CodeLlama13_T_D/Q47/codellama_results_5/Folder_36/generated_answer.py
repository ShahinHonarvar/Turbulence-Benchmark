
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(124, 283+1):
        for j in range(i+115-1, min(i+134, len(string))+1):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
