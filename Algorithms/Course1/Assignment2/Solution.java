import java.io.*;
import java.util.*;

public class Solution{
    private int[] data;
    private List<Integer> list;
    private long counter;

    Solution(){
        this.counter=0;
        this.list=new ArrayList<Integer>();
    }

    public static void main(String[] args) throws FileNotFoundException,IOException {
        String filePath="test.txt";
        //File file=new File("test.txt");
        //System.out.println(file.exists());
        //BufferedReader br = new BufferedReader(new FileReader(file));
        Solution s =new Solution();
        s.readTextInteger(filePath);
        s.run();
        System.out.println("Inversion result:"+s.counter);
        /*
        for(int i : s.getData()){
            System.out.print(i+" ;");
        }
        */
    }
    public void readTextInteger(String fpath) throws FileNotFoundException{
        try{
            File file=new File("test.txt");
            System.out.println(file.exists());
            BufferedReader br = new BufferedReader(new FileReader(file));
            String st = "";
            while (st != null){
                st =br.readLine();
                if(st == null){
                    break;
                }else{
                    this.list.add(Integer.parseInt(st.trim()));
                }
            }
            data = new int[list.size()];
            for(int i=0; i< list.size();i++){
                data[i]=(int) list.get(i);
            }
        }catch (FileNotFoundException e){
            System.out.println("Exception thrown  :" + e);
        }catch (IOException e){
            System.out.println("Exception thrown  :" + e);
        }
    }

    public void setData(int[] data) {
        this.data = data;
    }

    public int[] getData() {
        return data;
    }

    public long getCounter() {
        return counter;
    }

    public void run(){
        this.counter=0;
        splitSort(data,0,data.length);
    }

    private void splitSort(int[] data,int l,int r){
        // exclude r
        int m = (l+r)/2;
        if(l<r-1){
            splitSort(data, l,m);
            splitSort(data,m,r);
        }
        sortCount(data,l,m,r);
    }

    private void sortCount(int[] data, int l, int m ,int r){
        for(int j= m;j<r;j++){
            int i = j;
            while(i>l && data[i]<data[i-1]){
                int t = data[i];
                data[i]=data[i-1];
                data[i-1]=t;
                i--;
                this.counter++;
            }
        }
    }
}
