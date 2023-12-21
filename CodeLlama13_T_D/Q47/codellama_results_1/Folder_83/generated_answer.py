
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the given string
    palindromes = set()
    for i in range(75, 96):
        for j in range(i+7, i+10):
            if j > len(string):
                break
            substring = string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
