
import re

def palindromes_of_specific_lengths(s):
    subset = s[10:76]
    subset = re.sub('[^a-zA-Z]', '', subset)
    palindromes = set()
    
    for i in range(len(subset)):
        for j in range(i+10, min(i+21, len(subset)+1)):
            slice_string = subset[i:j]
            if slice_string.lower() == slice_string[::-1].lower():
                palindromes.add(slice_string)
    return palindromes
