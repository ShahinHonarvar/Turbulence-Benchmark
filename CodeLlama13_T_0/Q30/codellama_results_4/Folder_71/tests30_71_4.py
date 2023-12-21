from Q30.codellama_results_4.Folder_71.generated_answer import insert_before_character
import random
import string


def test_string_of_length_one():
    s = '2'
    assert insert_before_character(s) == 'S' + '2'


def test_large_string_of_only_specified_character():
    s = '2' * 1000
    assert insert_before_character(s) == ('S' + '2') * 1000


def test_length_of_large_string_of_only_specified_character():
    s = '2' * 1000
    assert len(insert_before_character(s)) == 2 * len(s)
    

def test_presence_of_inserted_character():
    s = ''.join(random.choices(string.ascii_letters + string.digits + ' ' * 10, k=1000))
    s = s + '2'
    returned_string = insert_before_character(s)
    assert 'S' in returned_string


def test_compare_length_of_strings():
    s = ''.join(random.sample(string.ascii_letters + string.digits, k=20))
    s = s + '2'
    returned_string = insert_before_character(s)
    assert len(s) < len(returned_string)
    

def test_length_of_result():
    s = ''.join(random.sample(string.ascii_letters + string.digits, k=20))
    s = s + '2'
    returned_string = insert_before_character(s)
    count = s.count('2')
    assert len(returned_string) == len(s) + count
    

def test_first_index_of_insert_char_in_result():
    s = ''.join(random.sample(string.ascii_letters + string.digits, k=20))
    s = s + '2'
    s = s.replace('S', '')
    returned_string = insert_before_character(s)
    assert returned_string.find('S') == s.find('2')


def test_all_indices_in_result():
    s = ''.join(random.choices(string.ascii_letters + string.digits + ' ' * 10, k=1000))
    s = s + '2'
    s = s.replace('S', '')
    returned_string = insert_before_character(s)
    indices_in_s = [i[0] for i in enumerate(s) if i[1] == '2']
    indices_in_returned_string = [i[0] for i in enumerate(returned_string) if i[1] == 'S']
    length = len(indices_in_s)
    assert length == len(indices_in_returned_string)
    l = [indices_in_s[i] + i for i in range(len(indices_in_s))]
    assert l == indices_in_returned_string
