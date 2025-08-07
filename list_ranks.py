# Rank every number in a list replacing every number with the corresponding
# rank
# EX: [9, 1, 6, 10] = [2, 4, 3, 1]

def ranks(intList: list):
    sorted_list = sorted(intList, reverse=True)
    rank_dict = {
        num: rank + 1
        for rank, num in enumerate(sorted_list)
    }
    out_ = [
        rank_dict[num]
        for num in intList
    ]
    return out_


intList = [9, 1, 6, 10]

ranks(intList)
