def remove_repeat_chars(str1):
    return str1[0:3] + str1[3:9].replace(" "*2,"") + str1[9:]
