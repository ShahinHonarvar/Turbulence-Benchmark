
def return_vowels(string):
    vowels_list = []
    vowels = "AEIOUaeiou"
    
    for char in string[44:95]:
        if char in vowels and "5" < char <= "<":
            vowels_list.append(char)
    
    return vowels_list
