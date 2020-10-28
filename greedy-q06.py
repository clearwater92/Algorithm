###
#이것이 코딩테스트다 교재의 p316 문제입니다.
###

import heapq

def solution(food_times, k):

    if sum(food_times) <= k:
        return -1

    q = []
    #[6, 8, 4] -> [(4,3),(6,1),(8,2)]
    #[8, 6, 4] -> [(4,3),(6,2),(8,1)]
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0
    previous = 0
    length = len(food_times)

    while (q[0][0]-previous) * length <= k - sum_value:
        now = heapq.heappop(q)[0]
        sum_value += (now-previous)*length
        length -= 1
        previous = now

    #음식 번호 순으로 나열
    result = sorted(q, key = lambda x: x[1])

    return result[(k-sum_value)%length][1]


print(solution([3,1,2], 5))
print(solution([8,6,4], 15))