
def filter_chars(string):
    filtered = ""

    for i in range(10, 70):

        if string[i] >= "I" and string[i] <= "K":

            continue


        else:


            filtered += string[i]


    return filtered
