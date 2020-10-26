
/**
 * Jeffrey Lansford
 * Exception Handling in Java
 * 10/6/20
 * Java program to test out the functionitly of exception handling
 */
import java.util.Scanner;

public class Grade {

    public static void main(String[] args) {

        int Freq[] = new int[10];
        int Index, New_Grade = 0, Limit_1, Limit_2;

        Scanner scan = new Scanner(System.in);

        while (true) {
            // take in value
            New_Grade = scan.nextInt();

            // exit loop if negitive number is inputted
            try {
                if (New_Grade < 0) {
                    throw new NullPointerException("Stop");
                }
            } catch (Exception e1) {
                break;
            }

            // exception handle to insert in array Freq
            try {
                throw new NullPointerException("Blah");
            } catch (Exception e2) {
                // calculate index
                Index = New_Grade / 10;
                // insert 100 into array as index equation would make it go beyond size of array
                if (New_Grade == 100) {
                    Freq[9] = Freq[9] + 1;
                }
                // Print for non-valid numbers and continue
                else if (New_Grade > 100) {
                    System.out.printf("Error -- new grade: %d is not vaild\n", New_Grade);
                }
                // store into array
                else {
                    Freq[Index] = Freq[Index] + 1;
                }
            }

        }

        // print frequencies of grades
        System.out.printf("%10s\t%10s\t%10s\n", "Limits Start", "Limits End", "Frequency");
        for (int i = 0; i < Freq.length; i++) {
            // calculate limits
            Limit_1 = 10 * i;
            Limit_2 = Limit_1 + 9;
            if (i == 9) {
                Limit_2 = 100;
            }
            System.out.printf("%10d\t%10d\t%10d\n", Limit_1, Limit_2, Freq[i]);
        }

    }
}
