import java.io.*;

public class FileConversion {
    public static void main(String[] args) {
        System.out.println("Java");
        FileInputStream fileInput;
        FileWriter fileOutput;
        try {
            fileInput = new FileInputStream("control-char.txt");
            fileOutput = new FileWriter("control-char-output.txt");
            int c;
            boolean deleteMode = false;
            while ((c = fileInput.read()) != -1) {
                if (c == 3) {
                    deleteMode = true;
                }
                if (!deleteMode) {
                    fileOutput.write(c);
                }
                // System.out.printf("Character: %d\n", c);
                if (c == 2) {
                    deleteMode = false;
                }

            }

            fileInput.close();
            fileOutput.close();
        } catch (Exception e) {
            System.out.println("File not found: " + e);
            return;

        }

    }
}