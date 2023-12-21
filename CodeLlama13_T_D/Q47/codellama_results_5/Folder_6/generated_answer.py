
def palindromes_of_specific_lengths(string):
    # find all palindromes in the substring from index 45 to index 98
    substr = string[45:99]
    palindromes = set()
    for i in range(40, 47+1):
        for j in range(len(substr) - i + 1):
            if substr[j:j+i] == substr[j+i-1::-1]:
                palindromes.add(substr[j:j+i])
    return palindromes
