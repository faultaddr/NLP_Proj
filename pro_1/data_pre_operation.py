import sys
def get_dict():
    fp = open("./data/data.txt", 'r', encoding="utf-8")
    str_list = []
    for line in fp.readlines():
        str_list.append(line.split("\n")[0].split("  ")[:-1])
    str_dic = {}
    fp.close()
    for s in str_list:
        key = s[0]
        str_dic[key] = s[1:]
    return str_dic
