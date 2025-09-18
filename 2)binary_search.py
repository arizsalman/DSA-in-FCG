
"""Loop  ya kyoe bhe conditon indexis pe kam karta he """


# def func(cards, target):
#     left, right = 0, len(cards)-1
#     while left <= right:
#         mid = (left+right)//2
#         mid_nums = cards[mid]
#         print(
#             f' left :{left} , right :{right} , mid_number :{mid_nums} ,mid : {mid}')
#         if mid_nums == target:
#             return mid
#         elif mid_nums > target:
#             left = mid+1
#         else:
#             right = mid-1
#     return -1


# #  ya ha hum test dictionary create kare ge
# test = {
#     'input': {

#         'cards': [13, 12, 10, 8, 7, 3],
#         'target': 8
#     },
#     'output': 3
# }

# # ab humare pass main function be agaya or values bhe a ge ab hum tested function banege


# def evaluate_test_case(func, test):
#     full_data = test['input']
#     expected_output = test['output']
#     actual_output = func(**full_data)
#     print(f'full_data {full_data}')
#     print(f'expected_output{expected_output}')
#     print(f'actual_output{actual_output}')
#     print(f'Test Result : Pass 'if {actual_output} == {
#           expected_output} else "FAIL ")

#     return actual_output


# result = evaluate_test_case(func, test)


# print("Result from function:", result)


# jab number bohat sare ho tu first number ko return karana hota he . Us me sab se best vo ye he do function bano .

def func1(card, query, mid):
    mid_number = card[mid]
    print(f' mid number :{mid_number} , mid :{mid}')
    if mid_number == query:
        if mid-1 >= 0 and card[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'right'
    else:
        return 'left'


def func2(card, query):
    left, right = 0, len(card)-1
    while left <= right:
        mid = (left+right)//2
        result = func1(card, query, mid)
        if result == 'found':
            return mid
            """ “right ko mid-1 karne se array aadha kat gaya aur right side ignore ho gayi”
                 bilkul, isi tarah binary search step by step search space aadha karta rehta hai."""
        elif result == 'left':
            right = mid-1
        elif result == 'right':
            left = mid+1
    return -1


print(func2([1, 2, 2, 6, 6, 6, 6, 6, 7, 7, 8, 8, 9], 7))

print(func2([1, 2, 2, 6, 6, 6, 6, 6, 7, 8, 9], 6))
