 def filter_chars(string):
    start = 164
    end = 706
    filtered_string = ""

    for i in range(start, len(string)):
        if string[i].isalpha():
            if (string[i] >= "O" and string[i] <= "}"):
                filtered_string += string[i]

    return filtered_string
