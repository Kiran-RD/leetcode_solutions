def allPathsSourceTarget(graph):
    n = len(graph)
    res = []

    def dfs(lst, path):
        nonlocal n

        if path[-1] == n - 1:
            res.append(path[:])
            return

        for i in range(len(lst)):
            dfs(graph[lst[i]], path+[lst[i]])

    dfs(graph[0], [0])
    return res

print(allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))








