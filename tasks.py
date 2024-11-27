def maximiseTasks(A, T):
    currentTime, numberOfTasks = 0,0
    A.sort()
    for i in range(len(A)):
        currentTime += A[i]
        if currentTime >= T:
            break
        numberOfTasks += 1
    return numberOfTasks

print(maximiseTasks([
    4,2,1,2,5
], 8))
print(maximiseTasks([
    3,1,7,4,9,2,5
], 23))