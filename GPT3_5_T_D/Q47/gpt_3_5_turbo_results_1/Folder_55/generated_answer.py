
def palindromes_of_specific_lengths(string):
    substr = string[10:76].lower()
    palindromes = set()
    for length in range(10, 21):
        for i in range(len(substr) - length + 1):
            if substr[i:i+length] == substr[i:i+length][::-1] and substr[i:i+length].isalpha():
                palindromes.add(substr[i:i+length])
    return palindromes
