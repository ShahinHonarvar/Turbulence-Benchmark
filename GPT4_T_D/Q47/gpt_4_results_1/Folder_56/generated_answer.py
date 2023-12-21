
def palindromes_of_specific_lengths(input_string):
    palindrome_set = set()
    
    for i in range(1,10):
        for j in range(i+3, min(8, 10-i)):
            substring = input_string[i:i+j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindrome_set.add(substring)
      
    return palindrome_set
