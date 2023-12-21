
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(45, 98+1):
        for j in range(i+40, i+47+1):
            if j-i <= len(string[i:j]) and string[i:j] == string[j-1:i-1:-1]:
                palindromes.add(string[i:j])
    return palindromes
