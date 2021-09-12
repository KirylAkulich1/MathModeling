from typing import Sequence
import method_middle_square

def tets_generator_for_test_case(func):
    test_cases = [[1234,2,23],[123456,6,123456],[1234567,3,345],[1234567,2,34]]
    for case in test_cases:
        func(*case)
    return lambda :None

def tests_cases_generator_for_middle_square_method(func):
    test_cases=[[1994,[9760,2576,6357,4114,9249,5440,5936,2360]]]
    for test_case in test_cases:
        func(*test_case)
    return lambda:None

@tets_generator_for_test_case
def get_middle_interval_should_return_expected_result(number:int,period_len:int,expected:int):

    result = method_middle_square.get_middle_interval(number,period_len)

    assert result == expected

@tests_cases_generator_for_middle_square_method
def middle_square_generator_should_generate_expected_sequane(seed,seq):
    method_iterator = method_middle_square.middle_square_generator(seed)
    generated_seq =[]
    for item in seq:
        generated_seq.append(next(method_iterator))
    print(generated_seq)
    assert generated_seq == seq

if __name__ =="__main__":
    get_middle_interval_should_return_expected_result()
    middle_square_generator_should_generate_expected_sequane()
