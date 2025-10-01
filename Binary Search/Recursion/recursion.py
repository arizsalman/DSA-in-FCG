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


"""Second Example in faster time compexity"""
"""ye actually Top-Down Dynamic Programming (Memoization) ka approach hai."""
"""Time Complexity = O(m * n)"""
"""Space Complexity: O(m * n)"""


def memo_func(seq1, seq2):
    memo = {}
    """ Yaha hum  hepler function koyon bante he !
     Helper function readability, simplicity aur extra parameter manage karne ke liye banaya jata hai.

     Technically bina helper ke bhi likh sakte ho, lekin code zyada cluttered aur confusing ban jayega.
       """
    def recursive(ind1, ind2):
        key = (ind1, ind2)
        if key in memo:
            return memo[key]
        elif ind1 == len(seq1) or ind2 == len(seq2):
            memo[key] = 0
        elif seq1[ind1] == seq2[ind2]:
            memo[key] = 1+recursive(ind1+1, ind2+1)
        else:
            memo[key] = max(
                recursive(ind1+1, ind2),
                recursive(ind1, ind2+1)
            )
        return memo[key]
    return recursive(0, 0)


print(memo_func(seq1="abcde", seq2="m"))  # ya equal naho tab zero age ga .
print(memo_func(seq1="abcde", seq2=""))  # ye empty ho tab zero age ga .
print(memo_func(seq1="serendipition", seq2="precipitation"))
print(memo_func(seq1="seen", seq2="seen"))
