def get_dict():
    str_list = []
    fp = open("./data/data.txt", 'r')
    for line in fp.readlines():
        str_list.append(line.split("\n")[0].split(","))
    str_dic = {}
    fp.close()
    for s in str_list:
        key = s[0]
        str_dic[key] = s[1:]
    return str_dic

