
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the substring
    palindromes = []
    for i in range(26, 85):
        substr = string[i:i+46]
        for j in range(0, len(substr)-1):
            if substr[j] == substr[len(substr)-1-j]:
                palindromes.append(substr[j:len(substr)-1-j])
    # Filter out palindromes of incorrect lengths and non-English letters
    filtered_palindromes = []
    for palindrome in palindromes:
        if len(palindrome) >= 30 and len(palindrome) <= 46:
            if all(c.isalpha() for c in palindrome):
                filtered_palindromes.append(palindrome)
    return filtered_palindromes
