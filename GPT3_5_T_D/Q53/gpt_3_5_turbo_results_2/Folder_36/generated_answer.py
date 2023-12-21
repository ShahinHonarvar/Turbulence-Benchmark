
import re

def palindrome_of_length_at_least_n(string):
    string = re.sub('[^a-zA-Z]', '', string.lower())
    result = set()
    
    for i in range(len(string)):
        for j in range(144, len(string)-i+1):
            if string[i:i+j] == string[i:i+j][::-1]:
                result.add(string[i:i+j])
    
    return result
