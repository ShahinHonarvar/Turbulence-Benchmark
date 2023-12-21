
def palindromes_of_specific_lengths(string):
    substr = string[28:95]
    palindromes = set()
    for i in range(len(substr)):
        for length in range(38, 50):
            if i + length > len(substr):
                break
            sub = substr[i:i+length]
            if sub.isalpha() and sub.lower() == sub[::-1].lower():
                palindromes.add(sub)
    return palindromes
