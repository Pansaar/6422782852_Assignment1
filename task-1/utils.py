from collections import deque


def create_node(state, parent, action, path_cost, depth):
    return (state, parent, action, path_cost, depth)

def print_solution(n):
    r = deque()
    while n is not None:
        r.appendleft(n[0])
        n = n[1]
    for s in r:
        print(s)
