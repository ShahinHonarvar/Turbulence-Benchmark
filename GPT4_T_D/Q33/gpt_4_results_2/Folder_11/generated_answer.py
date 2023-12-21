
def return_vowels(string):
    vowels = set("aeiouAEIOU")
    relevant_chars = string[29:73]
    filtered_chars = [char for char in relevant_chars if char > '#' and char<= '(' and char in vowels]
    return filtered_chars
