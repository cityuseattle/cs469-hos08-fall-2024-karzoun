# Activity-Selection-Problem
def activitySelection(start, finish):
    n = len(start)
    if n == 0: return [] 
   
    start, finish, actID = zip(*sorted(
        zip(start, finish, range(n)),
        key=lambda x: x[1]
    ))

    
    i, answer = 0, [actID[0]]

    for j in range(n):
        if start[j] >= finish[i]:
            answer.append(actID[j])
            i = j

    return answer

print(activitySelection(
    [0, 3, 4, 2, 5, -3, -9, 11, 10],
    [3, 4, 6, 8, 9, -12, -13, 14, 15]
))

print(activitySelection(
    [1, 3, 0, 5, 8, 5],
    [2, 4, 6, 7, 9, 9]
))

print(activitySelection(
    [4, 0, 1, 1, 3],
    [6, 2, 3, 6, 4]
))
