
//
// // from http://www.letmeknows.com/2017/04/24/wait-for-threads-to-finish-java/ //
// This is a very small set up to get people started on using threads
//
//
//
//
//  Adopted by Shaun Cooper
//  last updated November 2020
//
//  We need static variable pointers in the main class so that
//  we can share these values with the threads.
//  the threads are address separate from us, so we need to share
//  pointers to the objects that we are sharing and updating

/**
 * Jeffrey Lansford
 * 11/13/2020
 * Concurrecy
 * This program get N (size) from command line input and creates a NxN matrix and calculates max, min, and average of the matrix using threads
 * 
 */
import java.util.*;
import java.util.ArrayList;
import java.util.concurrent.TimeUnit;

public class MythreadTest {

    private static ArrayList<Thread> arrThreads = new ArrayList<Thread>();

    // we use static variables to help us connect the threads
    // to a common block
    public static int[][] A;

    // public varible to hold n^2
    public static float total_size;

    // arrays to allow threads to calcualte min. max, and average without a race
    // condition
    public static int min[];
    public static int max[];
    public static float average[];

    // main entry point for the process

    public static void main(String[] args) {
        try {
            // get size from command line input
            int size = Integer.parseInt(args[0]);
            // create the arrays from input
            A = new int[size][size];
            min = new int[size];
            max = new int[size];
            average = new float[size];

            // do n^2 for averge calculations
            total_size = size * (float) size;

            // fill array with random values
            Random rnd = new Random();
            for (int i = 0; i < A.length; i++) {
                for (int j = 0; j < A[i].length; j++) {
                    A[i][j] = (int) ((Math.pow(2, 32 - size) - Math.pow(2, 31 - size)) * rnd.nextFloat()
                            + Math.pow(2, 31 - size));
                }
            }

            // start timer
            long startTime = System.nanoTime();

            // create N threads to work on each row
            for (int i = 0; i < size; i++) {
                Thread T1 = new Thread(new ThreadTest(i));
                T1.start(); // standard thread start
                arrThreads.add(T1);
            }

            // wait for each thread to complete
            for (int i = 0; i < arrThreads.size(); i++) {
                arrThreads.get(i).join();
            }

            // all the threads are done
            // do final calculations
            // set base values to first element in arrays
            int max_Main = max[0];
            int min_Main = min[0];

            // find max and min in arrays that was calculated from the threads
            for (int i = 0; i < size; i++) {
                max_Main = Math.max(max_Main, max[i]);
                min_Main = Math.min(min_Main, min[i]);
            }

            // gets average of the whole matrix from adding the partial computed averages
            // from threads
            float total_average = 0;
            for (int i = 0; i < size; i++) {
                total_average += average[i];
            }

            // get end time
            long endTime = System.nanoTime();

            // calculate time elapsed for threads andmain to calculate max, min, and average
            long timeElapsed = endTime - startTime;

            // show output of time Elapsed, Max, Min, and Average
            System.out.println("Execution time in nanoseconds: " + timeElapsed);
            System.out.println("Execution time in milliseconds: " + timeElapsed / 1000000);
            System.out.printf("Max: %d\nMin: %d\nAverage: %f\n", max_Main, min_Main, total_average);

            // This for loop will not stop execution of any thread,
            // only it will come out when all thread are executed
            System.out.println("Main thread exiting ");
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}

// each thread should access its row based on "ind"
// and leave results I would suggest in a static array that you need
// to create in MythreadTest
// threads to calculate max, min and partail average per row
class ThreadTest implements Runnable {
    private int i;

    ThreadTest(int ind) {
        i = ind;
    }

    public void run() {
        try {
            // set base max and min
            MythreadTest.max[i] = MythreadTest.A[i][0];
            MythreadTest.min[i] = MythreadTest.A[i][0];

            // get max and min for row, and average of row with sum of i / n^2
            for (int j = 0; j < MythreadTest.A[i].length; j++) {
                MythreadTest.max[i] = Math.max(MythreadTest.A[i][j], MythreadTest.max[i]);
                MythreadTest.min[i] = Math.min(MythreadTest.A[i][j], MythreadTest.min[i]);
                MythreadTest.average[i] += MythreadTest.A[i][j] / MythreadTest.total_size;

            }

        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
