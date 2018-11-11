# -*- coding: UTF-8 -*-
import string
import re
import data_pre_operation
import sys
# 正向匹配
class SegmentSentence:

    def opt_sentence_forward(self,raw_input):
        str_dict, max_len = data_pre_operation.get_dict()
        word_list = []
        # 无法在词典中找到匹配词
        ill_word=0
        while len(raw_input) > 0:
            word = raw_input[0:max_len]
            record = False
            while (not record) and len(word) > 0:
                if word in str_dict:
                    word_list.append(word)
                    raw_input = raw_input[len(word):len(raw_input)]
                    record = True

                else:
                    ill_word+=1
                    if len(word) == 1:
                        word_list.append(word)
                        raw_input = raw_input[len(word):len(raw_input)]
                        record = True
                    else:
                        word = word[0:len(word) - 1]
        return word_list

    # 逆向匹配


    def opt_sentence_reverse(self,raw_input):
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
    def opt_sentence_result(self,raw_input):
        result_reverse=self.opt_sentence_reverse(raw_input)
        result_forward=self.opt_sentence_forward(raw_input)
        if result_forward== result_reverse:
            return result_reverse
        else:
            return  result_forward if len(result_reverse)>len(result_forward) else result_reverse


    def main(self):
        raw_input=sys.argv[1]
        while 1:
            print("--------××××××××：origin sentence: ××××××××--------       ",raw_input)
            result_list=self.opt_sentence_result(raw_input)
            print(' \033[1;35m ××××××××--------开始进行处理--------××××××× \033[0m')
            print("\n",' \033[1;36m 处理结果如下:--------××××××× \033[0m',"\n")
            for word in result_list:
                print(word, " / ", end=' ')
            print ("\n \n \n",' \033[1;35m ********press Enter to exit(or just continue)--------******** \033[0m',"\n")
            raw_input=input()
            if raw_input=="e" or raw_input=="E":
                sys.exit(0)


if __name__ == "__main__":
    seg=SegmentSentence()
    seg.main()
