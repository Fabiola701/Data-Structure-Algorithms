class stack:
    def __init__ (self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    def print(self):
        print(self.items)

def reverse_string(stack,input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])
    rev_str = ""
    while not stack.isEmpty():
        rev_str += stack.pop()
    return rev_str

stack = stack()
input_str = "Hello"
print(reverse_string(stack,input_str))