
def return_vowels(string):
    vowels = []
    for char in string[10:82]:
        if char > "$" and char <= "@" and char.lower() in "aeiou":
            vowels.append(char)
    return vowels
