def get_dict():
    max_len = 0
    str_list = []
    fp = open(r"./data/data.txt", 'r',encoding="gbk")
    for line in fp.readlines():
        str_list.append(line.split("\n")[0].split(","))
    str_dic = {}
    fp.close()
    for s in str_list:
        key = s[0]
        max_len = max(len(key), max_len)
        str_dic[key] = s[1:]
    return str_dic,max_len
