
def palindromes_of_specific_lengths(string):
    substr = string[11:88]
    substr = substr.lower()
    palindromes = set()
    for i in range(len(substr) - 3):
        if substr[i:i+4] == substr[i:i+4][::-1]:
            palindromes.add(substr[i:i+4])
        if i+5 < len(substr) and substr[i:i+5] == substr[i:i+5][::-1]:
            palindromes.add(substr[i:i+5])
    return palindromes
