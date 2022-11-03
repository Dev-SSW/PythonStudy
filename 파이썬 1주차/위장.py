def solution(clothes):
    cloth = {}
    answer = 1
    for i in clothes:
        if i[1] in cloth.keys():
            cloth[i[1]].append(i[0])S
        else:
            cloth[i[1]] = [i[0]]
        
    for j in cloth.values():
        answer *= len(j) + 1
    return answer-1
