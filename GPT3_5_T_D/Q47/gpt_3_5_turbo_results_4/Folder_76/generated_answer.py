
def palindromes_of_specific_lengths(string):
    substring = string[101:293] #exclusive end index is 293 since slices are exclusive
    substring = substring.lower() #converting substring to lowercase for case-insensitive comparison
    palindromes = set() #set to store the palindromes
    
    for length in range(154, 183): #iterating through the lengths from 154 to 182 (inclusive)
        for i in range(len(substring) - length + 1): #iterating through the substring with given length
            if substring[i : i + length] == substring[i : i + length][::-1]: #checking if the substring is palindrome
                if substring[i : i + length].isalpha(): #checking if the palindrome consists only of English letters
                    palindromes.add(substring[i : i + length]) #adding the palindrome to the set
    
    return palindromes
