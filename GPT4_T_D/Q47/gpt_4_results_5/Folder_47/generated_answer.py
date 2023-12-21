
def palindromes_of_specific_lengths(s):
    subset_string = s[39:95]
    palindrome_set = set()
    
    for i in range(len(subset_string)):
        for j in range(i+14, min(i+53, len(subset_string)+1)):
            substring = subset_string[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindrome_set.add(substring.lower())
    
    return palindrome_set
