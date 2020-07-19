import random
"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)

# cache will hold the results of calculations so i dont have to redo iterations
addition_dict = {}
subtraction_dict = {}


def f(x):
    return x * 4 + 6

# calculate all possible addition values of the list and store them in a dict
# calcualte all possible subtraction values of the list and store them in a dict
# then all i have to do is compare the two dicts - find where the values are the same and print their respective keys

random_choices = random.sample(q, k=4)
a, b, c, d = random_choices
# print(random_choices)
# print(a, b, c, d)

# [1, 2, 3, 4]   [10, 14, 18, 22]

def find_sums(num_list):
    for num in num_list:
        for second_num in num_list:
            if (num, second_num) in addition_dict:
                return addition_dict[f"{f(num)} + {f(second_num)}"]
            else:
                addition_dict[f"{f(num)} + {f(second_num)}"] = f(num) + f(second_num)
    return addition_dict

def find_diffs(num_list):
    for num in num_list:
        for second_num in num_list:
            if (num, second_num) in subtraction_dict:
                return subtraction_dict[f"{f(num)} - {f(second_num)}"]
            else:
                subtraction_dict[f"{f(num)} - {f(second_num)}"] = f(num) - f(second_num)
    return subtraction_dict

# print(find_sums(random_choices))
# print(find_diffs(random_choices)) 


# find where sums and differences are equal and print the combinations
def sum_diffs():
    find_sums(q)
    find_diffs(q)
    for add_key in addition_dict:
        for sub_key in subtraction_dict:
            if addition_dict[add_key] == subtraction_dict[sub_key]:
                print(f"{add_key} = {sub_key}")


sum_diffs()