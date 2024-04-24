graph=[(1,2,5),(2,3,4),(3,4,10),(4,5,6),(3,5,8)]
vertexset=set()
adj_mat=[]
for edge in graph:
    vertexset.add(edge[0])
    vertexset.add(edge[1])
nv=len(vertexset)
print("no of vertices=",nv)
adj_mat=[[0]*nv for i in range(nv)]
for row in adj_mat:
    print(row)
for edge in graph:
    adj_mat[edge[0]-1][edge[1]-1]=1
    adj_mat[edge[1]-1][edge[0]-1]=1
print("adj matrix")
for row in adj_mat:
    print(row)
    
