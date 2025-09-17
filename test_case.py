

"""ye code Example run karne ke le """


def anyvariable_name(cards, query):
    return cards.index(query)  # pehla index return karega


""" Ye Kaha kar rahe he hum  ?
 hum error ate  tu hum effecient cheez deke jis hum or logo se alag lege  : ye error bata tae, 
"""
test = {
    'input': {
        'cards': [13, 2, 4, 5, 7, 12, 4, 7],
        'query': 7
    },
    'output': 4
}
"""is ko run karne leye kya kare pehel hum jis pe langna he for example :
 anyvariable_name (test['input']['cards'],test['input']['query'])==test['output'] Ak Tareka ye he 
 anyvariable_name(**test['input'])==test['output'] ak ye bhe 

"""
print(anyvariable_name(**test['input']) == test['output'])  # True ya False

# Example no 2

# Function jo query ka index dhoondhe


def locate_card(cards, query):
    for i in range(len(cards)):
        if cards[i] == query:
            return i   # yaha return karna zaroori hai
    return -1   # agar query na mile


# Test case dictionary
test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}


def evaluate_test_case(func, test):
    input_data = test['input']
    expected_output = test['output']
    actual_output = func(**input_data)

    print("Input:", input_data)
    print("Expected Output:", expected_output)
    print("Actual Output:", actual_output)
    print("Test Result:", "PASS ✅" if actual_output ==
          expected_output else "FAIL ❌")
    return actual_output


def locate_card(cards, query):
    for i in range(len(cards)):
        if cards[i] == query:
            return i
    return -1


test = {
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 7
    },
    'output': 3
}

# test = {
#     'input': {
#         'cards': [13, 3, 5, 6, 8, 7, 1, 4, 0],
#         'query': 4
#     },
#     'output': 3
# }
# test = {
#     'input': {
#         'cards': [1,3,45,-9,2,0,,-2],
#         'query': 4
#     },
#     'output': -1
# }
# test = {
#     'input': {
#         'cards': [13, 3, 5, 6, 8, 7, 1, 4, 0],
#         'query': 4
#     },
#     'output': 0
# }
evaluate_test_case(locate_card, test)
# yaha first prameter locate_card ko is leye deya ke is ko test/run  karna he
# dusa  test ko is leye daya ke is pe test horaha he
# Pehla argument → jis cheez pe kaam karna hai (function)
# Dusra argument → jis ke sath kaam karna hai (test case data)


def locate_case(card, query):
    position = 0
    while position < len(card):
        if card[position] == query:
            return position
        position += 1
    return -1


print(locate_case([1, 2, 3, 4, 5, 6], 0))
