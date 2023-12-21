
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the given string
    palindromes = []
    for i in range(2, 8+1):
        for j in range(i, 9-i+1):
            if string[j] == string[i-1]:
                palindromes.append(string[i:j+1])
    
    # Filter out non-English letters and palindromes of incorrect length
    filtered_palindromes = []
    for palindrome in palindromes:
        if all(chr.isalpha() and chr.islower() for chr in palindrome) and 3 <= len(palindrome) <= 4:
            filtered_palindromes.append(palindrome)
    
    return set(filtered_palindromes)
