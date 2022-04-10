class MyStack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def parentheses(string):
    my_stack = MyStack()
    par_opened = ('(', '[', '{')
    par_closed = (')', ']', '}')
    opposite_par = {'(': ')', '[': ']', '{': '}'}

    for i in string:
        if i in par_opened:
            my_stack.push(i)
        if i in par_closed:
            if my_stack.isEmpty():
                return False
            if opposite_par[my_stack.peek()] == i:
                my_stack.pop()
            else:
                return False
    return my_stack.isEmpty()


my_string = '({})'

if parentheses(my_string) is True:
    print('Сбалансированно')
else:
    print('Несбалансированно')
