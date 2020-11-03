###
#이것이 코딩테스트다 교재의 p346 문제입니다.
###

def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer #1
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index+1:] #2
    if check_proper(u):# 3
        answer = u + solution(v) #3-1
    else: #4
        answer = '(' #4-1
        answer += solution(v) #4-2
        answer += ')' #4-3
        u = list(u[1:-1]) #4-4
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer #4-5
