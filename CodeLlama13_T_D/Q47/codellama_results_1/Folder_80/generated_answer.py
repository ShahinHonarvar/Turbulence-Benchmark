
def palindromes_of_specific_lengths(string):
    # find the substring from index 35 to index 88, both inclusive
    substr = string[35:89]
    
    # find all palindromes in the substring that have lengths between 24 and 33 (both inclusive)
    palindromes = []
    for i in range(len(substr)):
        for j in range(i+1, min(i+24, len(substr)+1)):
            if substr[i:j] == substr[i:j][::-1]:
                palindromes.append(substr[i:j])
    
    # return the set of all palindromes found in the substring that have lengths between 24 and 33 (both inclusive)
    return set(palindromes)
