station_qty = int(input())

generator_cost = list(map(int, input().split(' ')))

cable_qty = int(input())

#stations linked with cables of particular cost looks like weighted undirected graph
#cost of generator inside the station imagine as separate vertex with weighted edges to each station to receive connected graph
stations_sceme = []
gen_index = 0
for gen in range(1, station_qty + 1):
    stations_sceme.append([generator_cost[gen_index], 0, gen, ])
    gen_index += 1


for _ in range(cable_qty):
    st1, st2, cost = map(int, input().split(' '))
    #we put cost as first to simplify sorting, see below
    stations_sceme.append([cost, st1, st2])

#In this task we need to find a minimum spanning tree in a  edge-weighted undirected graph

#first we sort edges of a graph, by cost
stations_sceme.sort()

#in first step each vertex belongs to separate component
# final result: all vertices belong to one component
comp = [i for i in range(station_qty + 1)]
#variable to store sum of edges in the minimum spanning tree
Ans = 0
for weight, start, end in stations_sceme:
    # if start vertex and end vertex not in one component
    # add this edge in a tree , 
    if comp[start] != comp[end]:
        Ans += weight
        a = comp[start]
        b = comp[end]
        #after end vertex and start vertex belongs to one component (eg. a number of the component of the first vertex)
        for i in range(station_qty + 1):
            if comp[i] == b:
                comp[i] = a

print(Ans)
