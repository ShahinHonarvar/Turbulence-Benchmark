
import re

def palindrome_of_length_n(string):
    string = re.sub('[^a-zA-Z]', '', string)
    return set([string[i:i+46] for i in range(len(string)-45) if string[i:i+46].lower() == string[i:i+46].lower()[::-1]])
