def solution(participant, completion):
    sum = 0;
    HashTest = {}
    for a in participant:
        HashTest[hash(a)] = a
        sum += hash(a)
    for b in completion:
        sum -= hash(b)
    return HashTest[sum]
