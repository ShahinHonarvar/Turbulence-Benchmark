
def palindromes_of_specific_lengths(string):
    # Split the string into substrings of length 40-72
    substrs = [string[i:j] for i in range(15, 89) for j in range(i+40, i+73)]
    
    # Filter out non-palindromes and non-English letters
    palindromes = []
    for substr in substrs:
        if len(substr) % 2 == 1:
            continue
        mid = int((len(substr) - 1) / 2)
        if substr[:mid] != substr[mid+1:]:
            continue
        palindromes.append(substr)
    
    return set(palindromes)
