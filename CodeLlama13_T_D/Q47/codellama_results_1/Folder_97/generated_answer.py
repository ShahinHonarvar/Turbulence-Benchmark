
def palindromes_of_specific_lengths(string):
    substr = string[28:95]  # substring from index 28 to index 94, both inclusive
    palindromes = set()  # empty set for storing palindromes
    
    for i in range(38, 50):  # iterate over lengths between 38 and 49 (both inclusive)
        for j in range(len(substr)):  # iterate over the substring
            if substr[j:j+i] == substr[j:j+i][::-1]:  # check if the substring is a palindrome of length i
                palindromes.add(substr[j:j+i])  # add the palindrome to the set
    
    return palindromes  # return the set of all palindromes found in the substring
