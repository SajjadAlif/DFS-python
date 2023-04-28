print("Name: Sazzadul Hasan Alif\n Id: 18   Year: 4\n\n")
graph = {
  '5' : ['7','3'],
  '3' : ['4', '2'],
  '7' : [],
  '2' : [],
  '4' : ['7'],
  '8' : ['']
}
visited = set() 
def dfs(visited, graph, node):  
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
print("**********Welcome to Sazzadul Hasan Alif's DFS code************\n The Deth-First Search is ")
dfs(visited, graph, '5')