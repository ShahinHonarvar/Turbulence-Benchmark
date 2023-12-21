
def palindromes_of_specific_lengths(string):
    # Find the substring from index 18 to index 65, both inclusive
    substr = string[17:66]
    
    # Create a set of all palindromes with length between 23 and 36
    palindromes = {substr[i:i+j] for i in range(len(substr)) for j in range(23, 36) if substr[i:i+j] == substr[i:i+j][::-1]}
    
    # Return the set of palindromes that occur between index 18 and index 65, both inclusive
    return {palindrome for palindrome in palindromes if len(substr.lower().find(palindrome)) == len(palindrome)}
