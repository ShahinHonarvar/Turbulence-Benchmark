
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    relevant_chars = []
    for char in string[5:6]:
        if char in vowels and '3' < char <= '^':
            relevant_chars.append(char)
    return relevant_chars
