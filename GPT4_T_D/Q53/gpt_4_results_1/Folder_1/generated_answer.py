
def palindrome_of_length_at_least_n(string):
    import re
    string = string.lower()
    string = re.sub('[^a-z]','', string)
    palindromes = set()
    length = len(string)
    for i in range(length):    
        for j in range(i+29, length+1):   
            if string[i:j] == string[i:j][::-1]:    
                palindromes.add(string[i:j]) 
    return palindromes
