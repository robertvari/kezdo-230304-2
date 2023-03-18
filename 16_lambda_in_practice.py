name_list = ["Vári Róbert", "Kiss Elemér", "Nagy Adrienn", "Tóth Barna", "Kiss Elemér Aladár"]

def get_last_name(name):
    return name.split()[-1]

result_1 = sorted(name_list)
result_2 = sorted(name_list, key=get_last_name)
result_3 = sorted(name_list, key=lambda name: name.split()[-1])
print(result_1)
print(result_2)
print(result_3)
