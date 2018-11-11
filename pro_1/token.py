from __future__ import print_function
from  data_pre_operation import get_dict
import sys

class EnWord:

    def handle_error(self):
        print("------****** 本单词暂时还未被潘氏大辞典收录 ******------")

    def opt_rules(self, raw_str: str):
        """

        :param raw_str:
        :return:
        """
        temp1 = temp2 = temp3 = temp4 = ""
        if raw_str.endswith("s"):
            if raw_str[-3:-1] == 'ie':
                temp3 = raw_str[:-3] + "y"
            if raw_str[-2] == 'e':
                temp2 = raw_str[:-2]
            temp1 = raw_str[:-1]

        elif raw_str.endswith("ed"):
            if raw_str[-3] == 'i':
                temp3 = raw_str[:-3] + "y"
            if len(raw_str) >= 4 and raw_str[-4] == raw_str[-3]:
                temp4 = raw_str[:-3]
            temp1 = raw_str[:-2]
            temp2 = raw_str[:-1]

        elif raw_str.endswith("ing"):
            if raw_str[-4] == 'y':
                temp3 = raw_str[:-5] + 'ie'
            if len(raw_str) >= 5 and raw_str[-5] == raw_str[-4]:
                temp4 = raw_str[:-4]
            temp2 = raw_str[:-3]
            temp1 = raw_str[:-3] + 'e'
        else:
            temp = []
            fp = open("./data/v.txt", 'r')
            for line in fp.readlines():
                if raw_str in line.split():
                    temp.append(line[0])
            return temp
        return [temp1, temp2, temp3, temp4]

    def main(self):
        str_dict = get_dict()
        input_str=sys.argv[1]
        print("---------------****** 英语字典 ******---------------")
        print("本软件最终解释权归种菜的小朋友所有 @copyright")
        while(1):
            print("你想查询的英文单词为:  ",input_str,"\n")
            print("还原的英文单词为:")
            temp_str = input_str.split()
            for i in temp_str:
                if str_dict.get(i) is not None:
                    print(i, "  查询结果如下所示：----****----")
                    for j in range(len(str_dict[i])):
                        if j % 2 == 0:
                            print("  ", str_dict[i][j])
                        else:
                            print("    ", str_dict[i][j])
                else:
                    opted = self.opt_rules(i)
                    for x in opted:
                        if x != "":
                            if str_dict.get(x) is not None:
                                print(x, "  查询结果如下所示：----****----")
                                for j in range(len(str_dict[x])):
                                    if j % 2 == 0:
                                        print("  ", str_dict[x][j])
                                    else:
                                        print("    ", str_dict[x][j])
                        else:
                            pass
                    if len(opted) == 0:
                        self.handle_error()
            print("如果需要继续查询请直接输入 否则请按e|E退出")
            input_str=input()
            if input_str=="e"  or input_str=="E":
                sys.exit(0)


if __name__ == "__main__":
    en = EnWord()
    en.main()
