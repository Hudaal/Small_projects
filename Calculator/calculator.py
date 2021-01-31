import re

from container import Queue, Stack
from function import Function, Operator
import numpy


class calculator:
    def __init__(self):
        self.functions = {'EXP': Function(numpy.exp),
                          'LOG': Function(numpy.log),
                          'SIN': Function(numpy.sin),
                          'COS': Function(numpy.cos),
                          'SQRT': Function(numpy.sqrt),
                          'SQUARE': Function(numpy.square)}

        self.operators = {'PLUSS': Operator(numpy.add, 0),
                          'GANGE': Operator(numpy.multiply, 1),
                          'DELE': Operator(numpy.divide, 1),
                          'MINUS': Operator(numpy.subtract, 0)}
        self.output_queue = Queue()

    def RPN(self):
        stack = Stack()
        while not self.output_queue.is_empty():
            ele = self.output_queue.pop()
            if isinstance(ele, float):
                stack.push(ele)
            elif ele in self.functions.keys():
                ele2 = stack.pop()
                stack.push(self.functions[ele].execute(ele2))
            elif ele in self.operators.keys():
                ele2 = stack.pop()
                ele3 = stack.pop()
                stack.push(self.operators[ele].execute(ele3, ele2))
        return stack.pop()

    def shunting_yard(self, string_regn):
        op_strong = "GANGE,DELE"
        op_stack = Stack()
        for ele in string_regn:
            if ele.isdigit() or ele[0] == '-':
                self.output_queue.push(float(ele))
            elif ele in self.functions.keys() or ele == "(":
                op_stack.push(ele)
            elif ele == ")":
                num = op_stack.pop()
                while num != "(":
                    self.output_queue.push(num)
                    num = op_stack.pop()
            if ele in self.operators.keys():
                peek = op_stack.peek()
                if peek:
                    if peek in op_strong:
                        self.output_queue.push(op_stack.pop())
                op_stack.push(ele)
            # print(op_stack.items)
            # print(self.output_queue.items)
        while not op_stack.is_empty():
            self.output_queue.push(op_stack.pop())
            # print(self.output_queue.items)
        return self.RPN()

    def string_parser(self, text):
        text.replace(" ", "")
        regex = '[-A-Z/(*/)*a-z0-9]+'
        #regex = '[-A-Za-z0-9]+'
        list1 = re.findall(regex, text)
        list3 = re.findall('[/(*/)*]+', text)
        list2 = []
        count_par = 0
        for i in list1:
            if '(' in i:
                num = i.count('(')
                self.split_par(i, list2, '(', num, list3, count_par)
                count_par += 1
            elif ')' in i:
                num = i.count(')')
                self.split_par(i, list2, ')', num, list3, count_par)
                count_par += 1
            else:
                list2.append(i)
        # print(list2)
        return self.shunting_yard(list2)

    def split_par2(self, i, list2, par, num):
        start_par = i.split(par)
        count = 0
        for ele in start_par:
            if ele != "":
                print(ele)
                list2.append(ele)
                for j in range(num):
                    list2.append(par)
                count += 2
        if count > len(start_par) + 1 + num:
            list2.pop(-1)
        return list2

    def split_par(self, i, list2, par, num, list3, count_par):
        start_par = i.split(par)
        count = 0
        for ele in start_par:
            if ele != "":
                list2.append(ele)
                for i in range(len(list3[count_par])):
                    list2.append(par)
                count += 2
        if count > len(start_par) + 1 + num:
            list2.pop(-1)
        return list2


calc = calculator()
print(calc.string_parser(
    "((15 DELE (7 MINUS (1 PLUSS 1))) GANGE 3) MINUS (2 PLUSS (1 PLUSS 1))"))
print(calc.string_parser("EXP(1 PLUSS 2 GANGE 3)"))
text = input("Skriv din operasjon: ")
print(calc.string_parser(text))
