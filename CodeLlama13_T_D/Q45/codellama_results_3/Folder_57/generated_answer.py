
def palindromes_between_indices(string):
    # Get the set of all possible substrings of length 5 or more from the given string that occur between indices 2 and 5, both inclusive
    substring_set = {string[i:j+1] for i in range(len(string)-4) for j in range(i+4, len(string)+1)}
    
    # Get the set of all palindromes from the substrings by checking if each substring is equal to its reverse
    palindrome_set = {substring for substring in substring_set if substring == substring[::-1]}
    
    return palindrome_set
