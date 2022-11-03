def solution(nums):
    answer = 0
    maxleng = int(len(nums) / 2)
    l = set(nums)
    if len(l) <= maxleng:
        answer = len(l)
    else:
        answer = maxleng
    return answer
