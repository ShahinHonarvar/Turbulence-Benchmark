
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(32, 71+1):
        for j in range(i, min(len(string), i+21-1)+1):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])
    return palindromes
