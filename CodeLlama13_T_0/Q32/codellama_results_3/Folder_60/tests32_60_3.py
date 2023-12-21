from Q32.codellama_results_3.Folder_60.generated_answer import insert_after_character
import random
import string


def test_string_of_length_one():
    s = 'C'
    assert insert_after_character(s) == 'C' + 'P'


def test_large_string_of_only_specified_character():
    s = 'C' * 1000
    assert insert_after_character(s) == ('C' + 'P') * 1000


def test_length_of_large_string_of_only_specified_character():
    s = 'C' * 1000
    assert len(insert_after_character(s)) == 2 * len(s)


def test_presence_of_inserted_character():
    s = ''.join(random.choices(string.ascii_letters + string.digits + ' ' * 10, k = 1000))
    s = s + 'C'
    returned_string = insert_after_character(s)
    assert 'P' in returned_string


def test_compare_length_of_strings():
    s = ''.join(random.sample(string.ascii_letters + string.digits, 20))
    s = s + 'C'
    returned_string = insert_after_character(s)
    assert len(s) < len(returned_string)
    

def test_length_of_result():
    s = ''.join(random.sample(string.ascii_letters + string.digits, 20))
    s = s + 'C'
    returned_string = insert_after_character(s)
    count = s.count('C')
    assert len(returned_string) == len(s) + count
    

def test_first_index_of_insert_char_in_result():
    s = ''.join(random.sample(string.ascii_letters + string.digits, 20))
    s = s.replace('P', '')
    s = s.replace('C', '')
    s = 'C' + s
    returned_string = insert_after_character(s)
    if 'P' == 'C':
        assert returned_string.find('P') == 0
        assert returned_string.rfind('P') == 1
    else:
        assert returned_string.find('P') == 1


def test_all_indices_of_char_destination_in_result():
    s = ''.join(random.choices(string.ascii_letters + string.digits + ' ' * 10, k=1000))
    s = s + 'C'
    s = s.replace('P', '')
    returned_string = insert_after_character(s)
    indices_in_s = [i[0] for i in enumerate(s) if i[1] == 'C']
    indices_in_returned_string = [i[0] for i in enumerate(returned_string) if i[1] == 'P']
    length = len(indices_in_s)
    assert length == len(indices_in_returned_string)
    l = [indices_in_s[i] + i + 1 for i in range(len(indices_in_s))]
    assert l == indices_in_returned_string
