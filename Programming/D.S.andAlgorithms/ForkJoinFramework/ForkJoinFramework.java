import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ForkJoinPool;
import java.util.concurrent.RecursiveTask;
import java.util.concurrent.ExecutionException;
/** example of using ForkJoinFramework
 *  Target Function extends RecursiveTask<> class
 *  ForkJoinPool class
 *  fork()/join()
 * */


public class ForkJoinFramework {
    public static void main(String[] args){

        int nThreads = Runtime.getRuntime().availableProcessors();
        System.out.println("AvailableProcessors: "+nThreads);

        ForkJoinPool pool = new ForkJoinPool(nThreads);
        IntSum task = new IntSum(3000);
        long sum = pool.invoke(task);
        System.out.println("Sum is : "+sum);

        int[] numbers = new int[1000];

        for(int i = 0; i < numbers.length; i++) {
            numbers[i] = i;
        }

        ForkJoinPool forkJoinPool = new ForkJoinPool(nThreads);
        Long result = forkJoinPool.invoke(new Sum(numbers,0,numbers.length));
        System.out.println(result);
    }
}

class IntSum extends RecursiveTask<Long>{
    private int count;
    public IntSum(int count){
        this.count=count;
    }

    @Override
    protected Long compute(){
        long result = 0;

        if(this.count <=0 ){
            return 0L;
        }else if( this.count == 1 ){
            return (long) this.getRandomInteger();
        }

        List<RecursiveTask<Long>> forks=new ArrayList<>();
        for(int i=0;i<this.count;i++){
            IntSum subTask = new IntSum(1);
            subTask.fork();
            forks.add(subTask);
        }
        for(RecursiveTask<Long> subTask:forks){
            result=result+subTask.join();
        }
        return result;
    }

    private  int getRandomInteger(){
        return (int)(Math.random() * 1000);
    }

}

class Sum extends RecursiveTask<Long> {
    int low;
    int high;
    int[] array;

    Sum(int[] array, int low, int high) {
        this.array = array;
        this.low   = low;
        this.high  = high;
    }

    @Override
    protected Long compute() {

        if(high - low <= 10) {
            long sum = 0;

            for(int i = low; i < high; ++i)
                sum += array[i];
            return sum;
        } else {
            int mid = low + (high - low) / 2;
            Sum left  = new Sum(array, low, mid);
            Sum right = new Sum(array, mid, high);
            left.fork();
            long rightResult = right.compute();
            long leftResult  = left.join();
            return leftResult + rightResult;
        }
    }
}
