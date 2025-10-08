"""Leetcode no 72"""

# word1 = "horse", word2 = "ros"


# def funct(word1, word2):
#     dec = {}

#     def ins(ind1, ind2):
#         key = (ind1, ind2)
#         if key in dec:
#             return dec[key]
#         elif ind1 == len(word1) or ind2 == len(word2):
#             dec[key] = 0
#         elif word1[ind1] == word2[ind2]:
#             dec[key] = 1 + ins(ind1+1, ind2+1)
#         else:
#             dec[key] = max(ins(ind1+1, ind2), ins(ind1, ind2+1))
#         return dec[key]
#     return ins(0, 0)


# """This Answer is Wrong """
# print(funct(word1="horse", word2="ros"))


# def longestSubsequence(nums):
#     length = len(nums)
#     if nums.count(0) == length:
#         return 0

#     if nums != 0:
#         return length
#     else:
#         return length


# print(longestSubsequence([1, 2, 3]))


"""Practice Question """
"""“Jis function me hum loop lagate hain usme index normal 0 se start hota hai,
lekin recursion me (jisme condition hoti hai) hume manually index=0 dena padta hai. kyuon ke is me loop nahe chal raha hota he """


# def knapsack(capacity, weights, profit, ind=0):
#     if ind == len(weights):
#         return 0
#     elif weights[ind] <= capacity:
#         option1 = profit[ind] + \
#             knapsack(capacity-weights[ind], weights, profit, ind+1)
#         option2 = knapsack(capacity,  weights, profit, ind+1)
#         return max(option1, option2)
#     else:
#         return knapsack(capacity, weights, profit, ind+1)


# print(knapsack(capacity=165, weights=[23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
#       profit=[92, 57, 49, 68, 60, 43, 67, 84, 87, 72]))


"""Next Dynamic Programming """
"""We’re solving the 0/1 Knapsack problem using Dynamic Programming (Bottom-Up).
Let’s break it down:"""


def Knapsack_dp(capacity, weight, profit):
    result = [[0 for _ in range(capacity+1)] for _ in range(len(weight))]
    for ind in range(len(weight)):
        for c in range(capacity + 1):
            if ind == 0:
                result[ind][c] = 0 if weight[ind] > c else profit[ind]
            elif weight[ind] > c:
                result[ind][c] = result[ind-1][c]
            else:
                option1 = profit[ind] + result[ind-1][c-weight[ind]]
                option2 = result[ind-1][c]
                result[ind][c] = max(option1, option2)
    return result[-1][-1]


print(Knapsack_dp(capacity=165, weight=[23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
      profit=[92, 57, 49, 68, 60, 43, 67, 84, 87, 72]))
