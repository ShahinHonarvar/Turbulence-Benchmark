
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(29, 98+1):
        for j in range(i+5, min(len(string), i+10)):
            if string[i:j] == string[j-1:i-1:-1]:
                palindromes.add(string[i:j])
    return palindromes
