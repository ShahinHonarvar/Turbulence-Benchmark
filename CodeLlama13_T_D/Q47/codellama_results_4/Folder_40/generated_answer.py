
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(3, 6): # Only consider palindromes of lengths between 3 and 5 (both inclusive)
        for j in range(0, len(string)-i+1): # Only consider palindromes occurring in the substring from index 0 to index 5 (both inclusive)
            substr = string[j:j+i]
            if substr == substr[::-1]: # Check if the substring is a palindrome
                palindromes.add(substr)
    return palindromes
