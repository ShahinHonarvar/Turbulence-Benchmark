
def palindromes_of_specific_lengths(string):
    substr = string[44:100]
    palindromes = set()
    for length in range(13, 43):
        for i in range(len(substr) - length + 1):
            if substr[i:i+length].lower() == substr[i:i+length][::-1].lower():
                palindromes.add(substr[i:i+length])
    return palindromes
