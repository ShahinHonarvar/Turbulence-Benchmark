
def return_vowels(string):
    vowels = []
    for letter in string[11:53]:
        if letter > "+" and letter <= "W" and letter.lower() in "aeiou":
            vowels.append(letter)
    return vowels
