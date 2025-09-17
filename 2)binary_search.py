
"""Loop  ya kyoe bhe conditon indexis pe kam karta he """


def func(cards, target):
    left, right = 0, len(cards)-1
    while left <= right:
        mid = (left+right)//2
        mid_nums = cards[mid]
        if mid_nums == target:
            return mid
        elif mid_nums > target:
            left = mid+1
        else:
            right = mid-1
    return -1


#  ya ha hum test dictionary create kare ge
test = {
    'input': {

        'cards': [13, 12, 10, 8, 7, 3],
        'target': 8
    },
    'output': 3
}

# ab humare pass main function be agaya or values bhe a ge ab hum tested function banege


def evaluate_test_case(func, test):
    full_data = test['input']
    expected_output = test['output']
    actual_output = func(**full_data)
    print(f'full_data {full_data}')
    print(f'expected_output{expected_output}')
    print(f'actual_output{actual_output}')
    print(f'Test Result : Pass 'if {actual_output} == {
          expected_output} else "FAIL ")

    return actual_output


result = evaluate_test_case(func, test)


print("Result from function:", result)
