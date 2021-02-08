import os
import math

class Create_Brainfuck_Code:
    
    def  __init__(self, text:str):
        self.array = []
        for char in text:
            self.array.append(ord(char))
        self.MAX = 0
        self.list_ = []
        self.m = 10000000000
        self.flag = []
        self.bf_code = ''

    def max_Decision(self):
        for item in self.array:
            if self.MAX < item:
                self.MAX = item

    def decisive_decision(self):
        for i in range(self.MAX):
            if i == 0:
                continue
            sum_value = i 
            for ai in self.array:

                r1 = ai // i
                r2 = (ai + i) // i

                if ai - r1 * i > r2 * i - ai:
                    r = r2 * i - ai
                    sum_value += r2
                else :
                    r = ai - r1 * i
                    sum_value += r1

                sum_value = sum_value + r
                self.list_.append(sum_value)
    
    def m_decision(self):
        for i in range(len(self.list_)):
            #print(li)
            li = self.list_[i]
            if self.m > li:
                #print(li)
                self.m = li
                std = i

    def plus_write(self):
        for i in range(self.m):
            self.bf_code += '+'
        
    def for_write(self):
        self.bf_code += '['
        for ai in self.array:
            r1 = ai // self.m 
            r2 = (ai + self.m) // self.m 
            self.bf_code += '>'

            if ai - r1 * self.m > r2 * self.m - ai:
                self.flag.append(-(r2 * self.m - ai))
                for j in range(r2):
                    self.bf_code += '+'

            else:
                self.flag.append(ai - r1 * self.m)
                for j in range(r1):
                    self.bf_code += '+'

    def re_pointer2loop_counter(self):
        for i in range(len(self.array)):
            self.bf_code += '<'
        self.bf_code += '-'
        self.bf_code += ']'

    def round_up(self):
        for i in range(len(self.array)):
    
            self.bf_code += '>'
            if self.flag[i] < 0:
                for j in range(-self.flag[i]):
                    self.bf_code += '-'
            else:
                for j in range(self.flag[i]):
                    self.bf_code += '+'
            self.bf_code += '.'

    def new_line(self):
        self.bf_code += '>++++++++++++.'

    def create(self) -> str:
        if self.array != []:
            self.max_Decision()
            self.decisive_decision()
            self.m_decision()
            self.plus_write()
            self.for_write()
            self.re_pointer2loop_counter()
            self.round_up()
            self.new_line()
        else:
            pass
        return self.bf_code


if __name__ == '__main__':
    bfCode = '+++++++++++++++++[>++++>+++++++>+++++++>++>++++>++>++++++>++++++>++++++>++++++>++>++++++>+++++++>+++<<<<<<<<<<<<<<-]>--.>--.>---.>--.>+++++.>--.>++++++.>+++.>+++++.>-.>--.>+++.>---.>-----.>++++++++++++.'
    #code = Create_Brainfuck_Code('But I like it.').create()
    code = Create_Brainfuck_Code('').create()
    print(code)
    #print("aaaa")
    #print(bfCode)
    #if bfCode == code:
        #print('ok')