
import re

def palindromes_of_specific_lengths(string):
    selected_string = string[200:301]
    selected_string = re.sub('[^a-zA-Z]', '', selected_string).lower()

    palindromes_set = set()
    for i in range(0, len(selected_string)):
        for j in range(i+10, min(i+51, len(selected_string)+1)):
            substr = selected_string[i:j]
            if substr == substr[::-1]:
                palindromes_set.add(substr)
    return palindromes_set
