

```python
import numpy as np
import math
import os.path as path
```


```python
class Graph():
    _V=0;
    _adj={};
    
    #rtnRecorder=[]
    def __init__(self,v):
        self._V=v
        for i in range(1,v+1):
            self._adj[i]=[[],[]]
    
    def addEdge(self, src, des, weight):
        if len(self._adj[src][0])==0:
            self._adj[src][0].append(des)
            self._adj[src][1].append(weight)
        else:
            for i in range(0,len(self._adj[src][0])):
                if self._adj[src][0][i] == des:
                    print("Edge ",src,"->",des," re-add operation missed.")
                    break
                elif self._adj[src][0][i] > des:
                    self._adj[src][0].insert(i,des)
                    self._adj[src][1].insert(i,weight)
                    break   
                else:
                    self._adj[src][0].append(des)
                    self._adj[src][1].append(weight)
                    break    
                    
    def getV(self):
        return self._V
    
    def getAdj(self):
        return self._adj

    def printGraph(self,s,n):
        for i in range(s,s+n):
            print("Node ",str(i),": ")
            print("\t",self._adj[i][0])
            print("\t",self._adj[i][1])
            print("---" * 10)
```


```python
class Dijkstra():
    g=Graph(0)
    distS={}
    distU={}
    target=[]
    
    def __init__(self):
        pass
        
    def setGraph(self, graph):
        self.g=graph
        for i in range(1,graph.getV()+1):
            self.distU[i]=math.inf
    
    def setHeadNode(self,src):
        self.distS[src]=0
        del self.distU[src]
        self.updateEdgeDist(src)
        
        
    # private
    def updateEdgeDist(self,head):
        for i in range(len(self.g.getAdj()[head][0])):
            t_node=self.g.getAdj()[head][0][i]
            if t_node in self.distU:
                t=self.distS[head]+self.g.getAdj()[head][1][i]
                if t < self.distU[t_node]:
                    self.distU[t_node]=t
    # privateF
    def selectMinNode(self):
        node = min(self.distU, key=self.distU.get )
        if self.distU[node] == math.inf:
            pass
        else:
            self.distS[node]=self.distU[node]
            del self.distU[node]
            self.updateEdgeDist(node)
        
    def run(self):
        while len(self.distU)>0:
            self.selectMinNode()
            
    def printDistS(self):
        print("DistS:\n\t")
        for i in self.target:
            if i in self.distS:
                print("node", i,":", self.distS[i],sep = "",end="; ")  
       
    def printDistU(self,top=math.inf):
        print("DistU:\n\t")
        for i in self.target:
            if i in self.distU:
                print("node", i,":", self.distU[i],sep = "",end="; ")
                
    def setTarget(self,alist):
        self.target=alist
               
```


```python
dij=Dijkstra()
dij.setTarget([7,37,59,82,99,115,133,165,188,197])
g=Graph(200)
fp=path.abspath(r"E:\COURSERA\00 Algorithms\02 Graph Search Shortest Paths and Data Structures\week2\dijkstraData.txt")
with open(fp,'r') as f:
    read_data=f.read()

lines=read_data.split('\n')[0:-1]
for line in lines:
    src=int(line.split("\t")[0])
    nodes=line.split("\t")[1:-1]
    for node in nodes:
        des=int(node.split(',')[0])
        weight=int(node.split(',')[1])
        g.addEdge(src,des,weight)

g.printGraph(1,4)
dij.setGraph(g)
dij.setHeadNode(1)
dij.run()
dij.printDistS()
print()
dij.printDistU()
```

    Node  1 : 
    	 [11, 26, 80, 163, 170, 145, 200, 173, 92, 140, 160, 27, 40, 150, 61, 159, 198, 114, 104, 30, 99, 138, 169, 49, 125, 117, 55]
    	 [1913, 4122, 982, 8164, 2620, 648, 8021, 2069, 647, 546, 6461, 7905, 9047, 2183, 9146, 7420, 1724, 508, 6647, 4612, 2367, 7896, 8700, 2437, 2909, 2597, 6399]
    ------------------------------
    Node  2 : 
    	 [5, 42, 127, 170, 131, 172, 34, 30, 26, 6, 11, 17, 157, 159, 142, 182, 93]
    	 [8026, 1689, 9365, 9342, 7005, 1438, 315, 2455, 2328, 8847, 1873, 5409, 8643, 1397, 7731, 7908, 8177]
    ------------------------------
    Node  3 : 
    	 [6, 31, 41, 43, 57, 101, 91, 167, 106, 76, 122, 144, 44, 177, 119]
    	 [9006, 3031, 7212, 7313, 1239, 3381, 2483, 3877, 6521, 7729, 9640, 285, 2165, 7097, 7711]
    ------------------------------
    Node  4 : 
    	 [31, 70, 162, 195, 72, 126, 121, 118, 90, 127, 135, 159, 106, 52, 190, 78, 75, 116, 49, 107, 89, 54]
    	 [399, 5285, 3924, 2490, 6508, 2625, 7639, 3626, 9446, 6808, 7582, 6133, 4769, 9267, 7536, 8058, 7044, 6771, 619, 4383, 6363, 313]
    ------------------------------
    DistS:
    	
    node7:2599; node37:2610; node59:2947; node82:2052; node99:2367; node115:2399; node133:2029; node165:2442; node188:2505; node197:3068; 
    DistU:
    	
    
