def filter_chars(str1):
    for i in range(770, 970):
        if str1[i] >= '-' and str1[i] <= 'D':
            str1 = str1.replace(str1[i], "")
    return str1
