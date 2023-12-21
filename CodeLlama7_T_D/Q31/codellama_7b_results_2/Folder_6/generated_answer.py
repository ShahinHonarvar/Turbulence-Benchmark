
def if_perfect_num(my_list):
    try:
        if my_list[790].is_perfect():
            return True

    except AttributeError as e:
#        print("Error:", e)

    return False
