import java.io.*;
import java.util.*;

/****** Graph (directed, adjacency list)
 * Contains(BFS,DFS) implementation
 * Author:Shuaishuai Li
 * Date: 22 August, 2018
 * Ref: www.geeksforgeeks.org
 * */

public class Graph {
    // # of vertices
    private boolean directed;
    private int V;
    // Array  of lists for Adjacency List Representation
    private LinkedList<Integer> adj[];

    Graph(boolean d, int v) {
        directed = d;
        V = v;
        adj = new LinkedList[v];
        for (int i = 0; i < v; i++) {
            adj[i] = new LinkedList();
        }
    }

    Graph(int v) {
        this(true, v);
    }

    public static void main(String args[]) {
        Graph g = new Graph(4);
        g.addEdge(0, 1);
        g.addEdge(0, 2);
        g.addEdge(1, 2);
        g.addEdge(2, 0);
        g.addEdge(2, 0); // repeat add same edge(2,0) should be reported.
        g.addEdge(2, 3);
        g.addEdge(3, 3);
        g.DFSTest();
        g.BFSTest();
    }

    void DFSTest() {
        System.out.println("Following is Depth First Traversal " +
                "(starting from vertex 2)");

        DFS(2);
    }

    void BFSTest() {
        System.out.println("Following is Breadth First Traversal " +
                "(starting from vertex 2)");
        BFS(2);
    }

    void addEdge(int v, int w) {
        if (adj[v].contains(w)) {
            System.out.println("Repeat add edge " + v + " -> " + w + " is ignored;");
        } else {
            adj[v].add(w);
            if (!directed) {
                adj[w].add(v);
            }
        }
    }

    void DFS(int s) {
        boolean visited[] = new boolean[V];
        DFSRec(s, visited);
        System.out.print("End;\n");
    }

    void DFSRec(int v, boolean visited[]) {
        visited[v] = true;
        System.out.print(v + " --> ");

        Iterator<Integer> i = adj[v].listIterator();
        while (i.hasNext()) {
            int n = i.next();
            if (!visited[n]) {
                DFSRec(n, visited);
            }
        }
    }

    void BFS(int s) {
        boolean visited[] = new boolean[V];
        visited[s] = true;
        System.out.println("vertex:" + s + " is explored; ");
        LinkedList<Integer> q = new LinkedList();
        q.add(s);
        while (q.size() > 0) {
            int n = q.remove();
            visited[n] = true;
            Iterator<Integer> i = adj[n].listIterator();
            while (i.hasNext()) {
                int t = i.next();
                if (!visited[t]) {
                    visited[t] = true;
                    System.out.println("vertex:" + t + " is explored; ");
                    q.add(t);
                }
            }
        }
    }
}

