num_orders = int(input())

orders = []

for _ in range(num_orders):
    start, end, cost = map(int, input().strip().split(' '))
    orders.append([start, end, cost])


#In this task we will use the solution of a weighted interval scheduling task using dynamic programming approach


#function need to find nearest previous order without conflict with the current
def latestNonConflict(arr, i):
    j = i - 1
    while j >= 0:
        if(arr[j][1] <= arr[i][0]):
            return j
        else:
            j = j - 1
    return -1


def findMaxProfit(arr, n):
    #first we sort input array by order's end time
    arr.sort(key = lambda x: x[1])

    #an array where we store suboptimal solutions on each stage: optimal cost for each order separately
    memory = [None] * n
    #first element in the memory array is a first element in sorted input array
    memory[0] = arr[0][2]
    
    for i in range(1, n):
        #find cost using cost of current order and cost of previous compatible solution
        current_cost = arr[i][2]
        l = latestNonConflict(arr, i)
        if l != -1:
            current_cost += memory[l]
        #compare current cost and previous solution in the memory array
        memory[i] = max(current_cost, memory[i - 1])
    
    #final result cost will the last element in memory array  
    return memory[n - 1]


result = findMaxProfit(orders, num_orders)
print(result)

