
def if_contains_anagrams(str_list):
    str_list = [x.lower() for x in str_list if len(x)>=3]
    str_list = [''.join(sorted(x)) for x in str_list]
    count = 0
    for i in range(len(str_list)):
        for j in range(i+1, len(str_list)):
            if str_list[i] == str_list[j]:
                count += 1
    if count >= 85:
        return True
    else:
        return False
