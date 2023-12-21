
def palindrome_of_length_at_least_n(input_string):
    import re
    input_string = input_string.lower() 
    input_string = re.sub('[^a-z]', '', input_string)
   
    palindrome_set = set()
    
    for i in range(len(input_string)-47):
        for j in range(i+48, len(input_string)+1):
            substring = input_string[i:j]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    
    return palindrome_set
