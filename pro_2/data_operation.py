# -*- coding: UTF-8 -*-
import string
import re
import data_pre_operation

# 正向匹配


def opt_sentence_forward(raw_input):
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

# 逆向匹配


def opt_sentence_reverse(raw_input):
    str_dict, max_len = data_pre_operation.get_dict()
    word_list = []
    while len(raw_input) > 0:
        word = raw_input[-max_len:]
        record = False
        while(not record) and len(word) > 0:
            if word in str_dict:
                word_list.insert(0,word)
                raw_input = raw_input[:-len(word)]
                record = True
            else:
                if len(word) == 1:
                    word_list.insert(0,word)
                    raw_input = raw_input[:-len(word)]
                    record = True
                else:
                    word = word[1:]
    return word_list


# 双向匹配


def main():
    print("--------××××××××请输入想要分词的句子：××××××××--------")
    raw_input = input()
    result_list_reverse = opt_sentence_reverse(raw_input)
    result_list_forward = opt_sentence_forward(raw_input)
    print(' \033[1;35m ××××××××--------开始进行处理--------××××××× \033[0m')
    for word in result_list_reverse:
        print(word, " / ", end=' ')
    for word in result_list_forward:
        print(word, " / ", end=' ')


if __name__ == "__main__":
    main()
