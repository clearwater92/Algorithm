###
#이것이 코딩테스트다 교재의 p323 문제입니다.
###

#str = input()
strlist = ['aabbaccc','ababcdcdababcdcd','abcabcdede','abcabcabcabcdededededede','xababcdcdababcdcd']

def solution(s):
    #압축이 되지 않을 경우 answer가 정답
    answer = len(s)
    #1개 단위부터 압축 단위를 늘려가며 확인(1~len(s)//2)
    for step in range(1, len(s)//2 + 1):
        compressed = "" #compressed가 압축된 문자열
        prev = s[0:step] #앞에서부터 step만큼의 문자열 추출
        count = 1
        #단위 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            #이전 상태와 동일하다면 압축 횟수 증가
            if prev == s[j:j + step]:
                count+=1
            #다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]
                count = 1
        #남아 있는 문자열이 있을 수 있으므로(마지막 비교가 같을 경우) 한 번 더 해줘야 한다
        compressed += str(count) + prev if count >= 2 else prev
        #만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer,len(compressed))
    return answer

for i in strlist:
    print(solution(i))