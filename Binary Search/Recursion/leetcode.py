"""Leetcode no 72"""

# word1 = "horse", word2 = "ros"


def funct(word1, word2):
    dec = {}

    def ins(ind1, ind2):
        key = (ind1, ind2)
        if key in dec:
            return dec[key]
        elif ind1 == len(word1) or ind2 == len(word2):
            dec[key] = 0
        elif word1[ind1] == word2[ind2]:
            dec[key] = 1 + ins(ind1+1, ind2+1)
        else:
            dec[key] = max(ins(ind1+1, ind2), ins(ind1, ind2+1))
        return dec[key]
    return ins(0, 0)


"""This Answer is Wrong """
print(funct(word1="horse", word2="ros"))
