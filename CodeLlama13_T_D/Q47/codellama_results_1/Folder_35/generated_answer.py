
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(34, 91):
        for j in range(i+14, min(len(string), i+40)):
            if string[i:j] == string[i:j][::-1].lower():
                palindromes.add(string[i:j])
    return palindromes
