import java.util.*;
import java.lang.*;
import java.io.*;
/** Implement this task using BFS based on Directed Graph
* Author:Shuaishuai Li
* Date: 23. August, 2018
*/
class GFG {
    public static void main (String[] args) {
        Scanner kb = new Scanner(System.in);
        int t = kb.nextInt();
        Integer[] desSet=GFG.setCondition(t);
        int max = (int) Collections.max(Arrays.asList(desSet));
        DiGraph g=GFG.buildGraph(max);
        for(int i=0;i<desSet.length;i++){
            g.BFS(1,desSet[i]);
        }
    }
    public static Integer[] setCondition(int t){
        Scanner keyboard = new Scanner(System.in);
        Integer nodes[]=new Integer[t];
        for(int i=0;i<t;i++){
            nodes[i]=keyboard.nextInt();
            //System.out.println(nodes[i]);
        }
        return nodes;
    }

    public static DiGraph buildGraph(int n){
        if(n>1000 || n<1){
            System.out.println("Graph size settle error, Graph building failed");
        }
        DiGraph g = new DiGraph(n+1);
        for(int i=1; i<= (n+1)/3; i++){
            g.addEdge(i,3*i);
        }
        for(int i=1; i< n; i++){
            g.addEdge(i,i+1);
        }
        return g;
    }

}
class DiGraph{
    private boolean explored[];
    private int V;
    public LinkedList<Integer> adj[];

    DiGraph(int v){
        V=v;
        adj=new LinkedList[V];
        for(int i=0;i<v;i++){
            adj[i]=new LinkedList();
        }
    }

    public void addEdge(int src, int tar){
        adj[src].add(tar);
    }

    public void BFS(int src, int des){
        explored=new boolean[V];
        LinkedList<Integer> srcNodes = new LinkedList();
        LinkedList<Integer> subLayerNodes = new LinkedList();
        srcNodes.add(src);
        int lc=0; // Layer Count

        while(srcNodes.size()>0 && !explored[des]){
            int n = srcNodes.remove();
            if(!explored[n]){
                explored[n]=true;
                for(int i=0;i<adj[n].size();i++){
                    if(!explored[adj[n].get(i)]){
                        subLayerNodes.add(adj[n].get(i));
                    }
                }
            }
            if(srcNodes.size()==0){
                srcNodes=(LinkedList<Integer>) subLayerNodes.clone();
                subLayerNodes.clear();
                lc++;
            }
        }
        System.out.println(lc);
    }
}
