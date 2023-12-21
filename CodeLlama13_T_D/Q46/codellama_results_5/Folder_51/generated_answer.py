
def gcf_three_nums(list_of_positive_integers):
    return __gcf_three_nums(list_of_positive_integers, 21, 69, 41)

def __gcf_three_nums(list_of_positive_integers, i, j, k):
    gcf = 1
    for num in (list_of_positive_integers[i], list_of_positive_integers[j], list_of_positive_integers[k]):
        while num % gcf == 0:
            num /= gcf
        gcf = num
    return gcf
