"""Recursion :
  Recursion ek function ka khud ko call karna hota hai, jab tak ek base case na mil jaye.
Har recursive call problem ko thoda chhota banata hai, aur end me sab calls mil kar final answer dete hain.
"""


"""recursion kese kaam karta hai?

Recursion ka logic ye hai:

Function ek badi problem ko leke usko tod deta hai chhoti problem me.

Fir khud ko call karta hai taake chhoti problem solve ho jaye.

Jab base case milta hai, waha se solution wapas upar build hota hai."""


# def func(seq1, seq2, ind1=0, ind2=0):
#     if ind1 == len(seq1) or ind2 == len(seq2):
#         return 0
#     elif seq1[ind1] == seq2[ind2]:
#         return 1+func(seq1, seq2, ind1+1, ind2+1)
#     elif seq1[ind1] != seq2[ind2]:
#         return max(func(seq1, seq2, ind1+1, ind2),
#                    func(seq1, seq2, ind1, ind2+1)
#                    )


# print(func(seq1="serendipition", seq2="precipitation"))


"""ye actually Top-Down Dynamic Programming (Memoization) ka approach hai."""
"""Time Complexity = O(m * n)"""
"""Space Complexity: O(m * n)"""


# def memo_func(seq1, seq2):
#     memo = {}
#     """ Yaha hum  hepler function koyon bante he !
#      Helper function readability, simplicity aur extra parameter manage karne ke liye banaya jata hai.

#      Technically bina helper ke bhi likh sakte ho, lekin code zyada cluttered aur confusing ban jayega.
#        """
#     def recursive(ind1, ind2):
#         key = (ind1, ind2)
#         if key in memo:
#             return memo[key]
#         elif ind1 == len(seq1) or ind2 == len(seq2):
#             memo[key] = 0
#         elif seq1[ind1] == seq2[ind2]:
#             memo[key] = 1+recursive(ind1+1, ind2+1)
#         else:
#             memo[key] = max(
#                 recursive(ind1+1, ind2),
#                 recursive(ind1, ind2+1)
#             )
#         return memo[key]
#     return recursive(0, 0)


# print(memo_func(seq1="abcde", seq2="m"))  # ya equal naho tab zero age ga .
# print(memo_func(seq1="abcde", seq2=""))  # ye empty ho tab zero age ga .
# print(memo_func(seq1="serendipition", seq2="precipitation"))
# print(memo_func(seq1="seen", seq2="seen"))


"""Dynamic Programming Solution """


def get_helper(matrix, idex1, idex2):
    if idex1 < 0 or idex2 < 0:
        return 0
    else:
        return matrix[idex1][idex2]


def func_d(seq1, seq2):
    """[[0 for _ in range(i2)] for _ in range(i1)]
iska matlab hota hai:

Bahar wala loop (for _ in range(i1)): ye rows banata hai. Matlab total i1 rows hongi.

Andar wala loop (for _ in range(i2)): ye har row ke andar i2 elements (columns) banata hai."""

    """ 🔑 Rule yaad rakho:

Sabse pehle ek row banani hoti hai (andar wala loop)

Fir un rows ko ek matrix banane ke liye repeat karna hota hai (bahar wala loop)"""
    i1, i2 = len(seq1), len(seq2)
    results = [[0 for _ in range(i2)] for _ in range(i1)]
    for idex1 in range(i1):
        for idex2 in range(i2):
            if seq1[idex1] == seq2[idex2]:
                results[idex1][idex2] = 1+get_helper(results, idex1-1, idex2-1)
            else:
                results[idex1][idex2] = max(get_helper(results, idex1-1, idex2),
                                            get_helper(results, idex1, idex2-1))

    return results[-1][-1] if i1 > 0 and i2 > 0 else 0


print(func_d(seq1="serendipition", seq2="precipitation"))
print(func_d(seq1="abcde", seq2="m"))
print(func_d(seq1="abcde", seq2=""))
