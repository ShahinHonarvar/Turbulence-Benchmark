
def palindromes_of_specific_lengths(string):
    palindromes = set()
    sub_string = string[65:100].lower()
    
    for i in range(len(sub_string)-33):
        for j in range(26, 34):
            palindrome = sub_string[i:i+j]
            
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    
    return palindromes
