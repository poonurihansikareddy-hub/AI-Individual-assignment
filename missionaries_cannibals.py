from collections import deque
import time

# Initial and Goal States
# State = (Missionaries_left, Cannibals_left, Boat_side)
# Boat_side: 0 = Left bank, 1 = Right bank

START = (3, 3, 0)
GOAL = (0, 0, 1)

MOVES = [(1,0),(2,0),(0,1),(0,2),(1,1)]


def valid(state):
    m, c, _ = state

    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    if m > 0 and c > m:
        return False

    if (3-m) > 0 and (3-c) > (3-m):
        return False

    return True


def successors(state):

    m, c, boat = state
    result = []

    for dm, dc in MOVES:

        if boat == 0:
            new = (m-dm, c-dc, 1)
        else:
            new = (m+dm, c+dc, 0)

        if valid(new):
            result.append(new)

    return result


# ---------------- BFS ----------------

def bfs():

    queue = deque([(START,[START])])
    visited = {START}
    nodes = 0

    while queue:

        state, path = queue.popleft()
        nodes += 1

        if state == GOAL:
            return path, nodes

        for nxt in successors(state):

            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, path+[nxt]))

    return None, nodes


# ---------------- DFS ----------------

def dfs():

    stack = [(START,[START],{START})]
    nodes = 0

    while stack:

        state, path, visited = stack.pop()
        nodes += 1

        if state == GOAL:
            return path, nodes

        for nxt in successors(state):

            if nxt not in visited:
                stack.append((nxt, path+[nxt], visited|{nxt}))

    return None, nodes


# ---------------- IDDFS ----------------

def dls(state, path, visited, limit):

    if state == GOAL:
        return path

    if limit == 0:
        return None

    for nxt in successors(state):

        if nxt not in visited:

            result = dls(nxt, path+[nxt], visited|{nxt}, limit-1)

            if result:
                return result

    return None


def iddfs():

    nodes = 0

    for depth in range(20):

        nodes += depth
        result = dls(START,[START],{START},depth)

        if result:
            return result, nodes

    return None, nodes


# ---------------- PRINT ----------------

def show(name, path, nodes, time_taken):

    print("\n"+"="*45)
    print(name)
    print("="*45)

    print("Steps:", len(path)-1)
    print("Nodes Explored:", nodes)
    print("Time:", round(time_taken,4),"ms")

    print("\nSolution Path:\n")

    for i,(m,c,b) in enumerate(path):

        left_boat  = "<boat>" if b==0 else ""
        right_boat = "<boat>" if b==1 else ""

        print(f"{i}. Left[{m}M {c}C] {left_boat} ~~~~ {right_boat} Right[{3-m}M {3-c}C]")


# ---------------- MAIN ----------------

print("\nMissionaries and Cannibals Problem")

results = []

for name, algo in [("BFS",bfs),("DFS",dfs),("IDDFS",iddfs)]:

    start = time.perf_counter()
    path,nodes = algo()
    elapsed = (time.perf_counter()-start)*1000

    results.append((name,path,nodes,elapsed))
    show(name,path,nodes,elapsed)


print("\n"+"="*45)
print("Algorithm   Steps   Nodes   Time(ms)")
print("="*45)

for name,path,nodes,t in results:

    print(f"{name:<10}{len(path)-1:<8}{nodes:<8}{round(t,4)}")