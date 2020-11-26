n = int(input())
str_list = []

for i in range(n):
    str_list.append(input())

def is_vps(str):
    stack = []
    for i in range(len(str)):
        if str[i] == '(':
            stack.append('(')
        else:
            if len(stack) == 0 or stack[-1] == ')':
                return 'NO'
            else:
                stack.pop()
    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'

for i in range(len(str_list)):
    print(is_vps(str_list[i]))