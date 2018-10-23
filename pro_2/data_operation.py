# -*- coding: UTF-8 -*-
import string
import re
from pro_2 import data_pre_operation


def opt_sentence(raw_input):
    str_dict, max_len = data_pre_operation.get_dict()
    word_list = []
    while len(raw_input) > 0:
        word = raw_input[0:max_len]
        record = False
        while (not record) and len(word) > 0:
            if word in str_dict:
                word_list.append(word)
                raw_input = raw_input[len(word):len(raw_input)]
                record = True

            else:
                if len(word) == 1:
                    word_list.append(word)
                    raw_input = raw_input[len(word):len(raw_input)]
                    record = True
                else:
                    word = word[0:len(word) - 1]
    return word_list


def main():
    print("--------××××××××请输入想要分词的句子：××××××××--------")
    raw_input = input()
    result_list = opt_sentence(raw_input)
    print(' \033[1;35m ××××××××--------开始进行处理--------××××××× \033[0m')
    for word in result_list:
        print(word, " / ", end=' ')


if __name__ == "__main__":
    main()
