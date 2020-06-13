#M - passengers, N - taxi drivers, K - base price, P - decrease coef (P - I), I - distace between driver and passender
M, N, P, K = map(int, input().split(' '))

#infinite value if there is no way between points
INF = 10**9

#ways between drivers and passengers, and between passengers represent as weighted directed graph
#w - adj. matrix
w = [[INF] * (N + M) for i in range(N + M)]

#S distanses from driver to passenger
S = int(input())

for _ in range(S):
    taxi, passenger, distance = map(int, input().split(' '))
    w[taxi][N + passenger] = distance


#T distanses between passengers
T = int(input())


for _ in range(T):
    pass_1, pass_2, distance = map(int, input().split(' '))
    w[N + pass_1][N + pass_2] = distance


prices = [K] * (N + M)

#In this task we implement Dijkstra's algorithm 
#IMPORTANT: this task doesn't solved to the end due to time-limit during some tests
#solution not optimal
for driver in range(N):
    dist = [INF] * (N + M)
    checked_clients = [False] * (N + M)
    dist[driver] = 0
    min_vertex = driver
    min_dist = 0
    while min_dist < INF:
        i = min_vertex
        checked_clients[i] = True
        for j in range(N, N + M):
            if dist[i] + w[i][j] < dist[j]:
                dist[j] = dist[i] + w[i][j]
        min_dist = INF
        for j in range(N, N + M):
            if not checked_clients[j] and dist[j] < min_dist:
                min_dist = dist[j]
                min_vertex = j
    for j in range(N, N + M):
        if dist[j] < INF:
            if dist[j] < P:
                delta = P - dist[j]
                prices[j] = prices[j] - delta   
    
print(min(prices))

