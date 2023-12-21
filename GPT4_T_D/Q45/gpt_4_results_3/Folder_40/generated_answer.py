
from itertools import permutations

def palindromes_between_indices(string):
    # Extracting the relevant part of the string
    sub_string = string[4:10].lower()
    
    # Initiating an empty set to store the palindromes
    palindromes = set()

    # Looping through permutations of the sub-string 
    # with length >= 7 and <= length of the actual sub-string
    for i in range(7, len(sub_string)+1):
        perm = permutations(sub_string, i)
        
        # Forming the variations from the permutations
        # Check if it is a palindrome and then add to the set
        for j in list(perm):
            temp_str = ''.join(j)
            if temp_str == temp_str[::-1]:
                palindromes.add(temp_str)

    return palindromes
