n = int(input())
stack = []
result = []
for _ in range(n):
    v = input()
    if v[:4] == 'push':
        stack.append(int(v[5:]))
    elif v[:3] == 'pop':
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack.pop())
    elif v[:4] == 'size':
        result.append(len(stack))
    elif v[:5] == 'empty':
        if stack:
            result.append(0)
        else:
            result.append(1)
    elif v[:3] == 'top':
        if len(stack) == 0:
            result.append(-1)
        else:
            result.append(stack[len(stack)-1])

for a in result:
    print(a)