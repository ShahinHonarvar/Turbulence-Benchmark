
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the substring from index 16 to index 77
    substr = string[16:78]
    palindromes = []
    for i in range(43, 48):
        for j in range(len(substr) - i + 1):
            if substr[j:j+i].lower() == substr[j:j+i][::-1]:
                palindromes.append(substr[j:j+i])
    return set(palindromes)
