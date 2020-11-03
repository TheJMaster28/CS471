/**
    Jeffrey Lansford
    11/2/2020
    Program 7
    Java version of removing content from file when seeing a Control-C and stopping when seeing a Control-B
 */
import java.io.*;

public class FileConversion {
    public static void main(String[] args) {
        // setup input and output objects
        FileInputStream fileInput;
        FileWriter fileOutput;
        try {
            
            // get input and output from command line arguments
            fileInput = new FileInputStream(args[0]);
            fileOutput = new FileWriter(args[1]);
            
            // acsii value of charcter being read
            int c;

            // set to write mode
            boolean deleteMode = false;
            // read in each charcter from file input stream
            while ((c = fileInput.read()) != -1) {

                //  set to delete mode when seeing a Control-C character ascii value
                if (c == 3) {
                    deleteMode = true;
                }

                // write to output fileif in write mode
                if (!deleteMode) {
                    fileOutput.write(c);
                }
                //  set to write mode when seeing a Control-B character ascii value
                if (c == 2) {
                    deleteMode = false;
                }

            }
            // close files
            fileInput.close();
            fileOutput.close();
        }
        //  catch any errors 
        catch (Exception e) {
            System.out.println("File not found: " + e);
            return;

        }

        System.out.println("Successfully wrote to " + args[1]);
    }
}