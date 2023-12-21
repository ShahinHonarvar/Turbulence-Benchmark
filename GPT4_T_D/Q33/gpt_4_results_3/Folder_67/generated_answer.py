
def return_vowels(my_string):
    vowels = ['a','e','i','o','u']
    selected_chars = []

    for char in my_string[21:59]:
        if char in vowels and char > '/' and char <= 'a':
            selected_chars.append(char)
    
    return selected_chars
