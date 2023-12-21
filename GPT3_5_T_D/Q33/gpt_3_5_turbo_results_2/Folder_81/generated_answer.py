
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 20
    end_index = 43
    filtered_vowels = []
    
    for index in range(start_index, end_index):
        if index > 5 and index <= ord('M'):
            letter = string[index]
            if letter.lower() in vowels:
                filtered_vowels.append(letter)
    
    return filtered_vowels
