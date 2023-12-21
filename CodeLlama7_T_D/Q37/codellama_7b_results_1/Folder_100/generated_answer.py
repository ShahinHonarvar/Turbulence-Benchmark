 def filter_chars(my_string):
    result = ""
    for i in range(len(my_string)):
        if my_string[i].isalpha():
            if (ord(my_string[i]) >= 74 and ord(my_string[i]) <= 81) or (ord(my_string[i]) >= 83 and ord(my_string[i]) <= 90):
                continue

        result += my_string[i]
    return result
