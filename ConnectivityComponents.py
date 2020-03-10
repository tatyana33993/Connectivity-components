#!/usr/bin/env python3
import copy
adjacency_list = []
visited = []
components = []


def dfs(u):
    visited[u] = True
    components.append(u)
    for v in adjacency_list[u]:
        if not visited[v]:
            dfs(v)


def find_components(filename):
    f = open(filename, 'r', encoding='utf-8')
    num = 0
    for line in f:
        if num == 0:
            adjacency_list.append(int(line))
        else:
            vertex_list = []
            k = 1
            for el in line:
                if el == '1':
                    vertex_list.append(k)
                k += 1
            adjacency_list.append(vertex_list)
        num = num + 1
    for u in range(0, adjacency_list[0] + 1):
        visited.append(False)
    result = []
    for v in range(1, adjacency_list[0] + 1):
        if not visited[v]:
            components.clear()
            dfs(v)
            result.append(copy.copy(components))
    f.close()
    f = open('out.txt', 'w', encoding='utf-8')
    f.write(str(len(result)) + '\n')
    out = ''
    for el in result:
        for k in el:
            out += str(k)
        out += '0\n'
    f.write(out[:-2])
    f.close()


if __name__ == '__main__':
    find_components('in.txt')
