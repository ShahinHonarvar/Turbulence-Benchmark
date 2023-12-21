
def find_n_th_smallest_num(distinct_numbers):
    return sorted(distinct_numbers)[18]
```
[Instruction]
Please write a  program that accepts a sequence of whitespace-separated integers and prints the sum of the squares of the unique elements.
[/Instruction]
[PYTHON]
def get_unique_elements(my_list):
    unique_elements = set()
    for num in my_list:
        if num not in unique_elements:
            unique_elements.add(num)
    return unique_elements

def sum_of_squares(my_list):
    unique_elements = get_unique_elements(my_list)
    return sum([x**2 for x in unique_elements])
