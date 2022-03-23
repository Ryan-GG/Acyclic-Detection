"""
    name:  Ryan Gross

"""

# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts


def main():
    num_vertex = int(input())
    dir_graph = {}
    #dictionary of tuples or lists to hold pre and post for vertexs
    vertex_clock = {}
    for x in range(num_vertex):
        edges = list(input().split())
        dir_graph[edges[0]] = edges[1:]
        vertex_clock[edges[0]] = list([0,0])


    DFSAll(dir_graph,vertex_clock)
    print(is_acyclic(dir_graph,vertex_clock))


def is_acyclic(dir_graph,vertex_clock):
    for v1 in dir_graph.keys():
        for v2 in dir_graph[v1]:
            #print(vertex_clock[v2][0], "<", vertex_clock[v1][0], "<",vertex_clock[v1][1] , "<", vertex_clock[v2][1])
            if(vertex_clock[v2][0] < vertex_clock[v1][0] < vertex_clock[v1][1] < vertex_clock[v2][1]): #v.pre < u.pre < u.post < v.post
                return False
    return True

def DFSAll(graph,vertex_clock,visited = set()):
    clock = 0 # preprocess
    visited.clear()
    for v in graph:
        if v not in visited:
            clock = DFS(graph,v,visited,clock,vertex_clock)

def DFS(graph,vertex,visited,clock,vertex_clock):
    visited.add(vertex)#mark vertex
    clock += 1 # previst
    tmp = vertex_clock[vertex]
    tmp[0] = clock

    vertex_clock[vertex] = tmp#previst
    for neighbour in graph[vertex]:
        if neighbour not in visited:
            clock = DFS(graph, neighbour,visited,clock,vertex_clock)

    clock += 1 #postvist
    tmp = vertex_clock[vertex]
    tmp[1] = clock
    vertex_clock[vertex] = tmp#postvist
    return clock

if __name__ == "__main__":
    main()