
def find_second_smallest_num(numbers):
    try:
        sub_list = numbers[31:35]
        sub_list.sort()
        return sub_list[1]
    except IndexError:
        return None
    except:
        return None
