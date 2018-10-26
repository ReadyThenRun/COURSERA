import java.util.Arrays;

/** MergeSort
 *  author: Shuaishuai Li
 *  date: 17 August, 2018
 *  ******** How to use example **************
 *      public static void main(String[] args) {
 *          // Generate a random number array using static method
 *         Integer[] array = MergeSort.randomIntArray(10, 100, 1000);
 *         // Using the target array as a parameter, Create an instance
 *         MergeSort test = new MergeSort(array);
 *         // Using sort method realize the sort process
 *         test.sort();
 *         test.print();
 *     }
 */

public class MergeSort {
    private Integer[] rawInputArray;
    private Integer[] sortedArray;
    private Integer invCounter;

    // Non parameter Constructor
    public MergeSort() {
        invCounter = 0;
    }

    // Constructor
    public MergeSort(Integer[] array) {
        invCounter = 0;
        rawInputArray = array.clone();
        sortedArray = array.clone();
    }

    public void print() {
        this.printArray(sortedArray, 0, sortedArray.length);
    }

    public void printArray(Integer[] array, int start, int end) {
        for (int i = start; i < end; i++) {
            System.out.print(array[i] + ", ");
        }
        System.out.print("\n");
    }

    public static void main(String[] args) {
        Integer[] array = MergeSort.randomIntArray(10, 100, 1000);
        MergeSort test = new MergeSort(array);
        test.sort();
        test.print();
    }

    public static Integer[] randomIntArray(int size, int min, int max) {
        Integer[] result = new Integer[size];
        for (int i = 0; i < size; i++) {
            result[i] = (Integer)(int)(long)Math.round(Math.random() * (max - min) + min);
        }
        return result;
    }

    public void sort() {
        sort(this.sortedArray, 0, this.sortedArray.length);
    }

    private void sort(Integer[] input, int start, int end) {
        if (end - start > 1) {
            int middle = (start + end + 1) / 2;
            sort(input, start, middle);
            sort(input, middle, end);
            merge(input, start, end);
        }
    }

    private void merge(Integer[] input, int start, int end) {
        Integer[] arrayCopy = Arrays.copyOfRange(input, start, end);
        int middle = (arrayCopy.length + 1) / 2;
        int i = 0;
        int j = middle;
        int wptr = start;
        for (; i < middle && j < arrayCopy.length; ) {
            System.out.println("i:" + i+"; j:"+j+"; middle:"+middle+"; end:"+end);
            if (arrayCopy[i] <= arrayCopy[j]) {
                input[wptr] = arrayCopy[i];
                i++;
            } else if (arrayCopy[i] > arrayCopy[j]) {
                input[wptr] = arrayCopy[j];
                j++;
            }
            wptr++;
        }
        while (i == middle && j < arrayCopy.length) {
            input[wptr] = arrayCopy[j];
            j++;
            wptr++;
        }
        while (i < middle && j == arrayCopy.length) {
            input[wptr] = arrayCopy[i];
            i++;
            wptr++;
        }
    }

    public void setInputArray(Integer[] inputArray) {
        rawInputArray = inputArray.clone();
        sortedArray = inputArray.clone();
    }

    public Integer[] getRawInputArray() {
        return rawInputArray;
    }

    public Integer[] getSortedArray() {
        return sortedArray;
    }

    public Integer getInvCounter() {
        return invCounter;
    }
}



