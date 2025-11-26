import java.util.Random;
import java.util.Scanner;

public class RockPaperScissors {
    private static int determineWinner(int player, int computer) {
        if (player == computer) return 0; // draw
        if ((player == 1 && computer == 3) || // rock beats scissors
            (player == 2 && computer == 1) || // paper beats rock
            (player == 3 && computer == 2)) { // scissors beats paper
            return 1; // player wins
        }
        return -1; // computer wins
    }

    private static String choiceToString(int choice) {
        switch (choice) {
            case 1: return "Rock";
            case 2: return "Paper";
            case 3: return "Scissors";
            default: return "Unknown";
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        System.out.println("Rock-Paper-Scissors (Java)");

        while (true) {
            System.out.println();
            System.out.println("1) Rock  2) Paper  3) Scissors  0) Quit");
            System.out.print("Your choice: ");

            if (!scanner.hasNextInt()) {
                scanner.nextLine(); // discard invalid input
                System.out.println("Invalid input. Please enter a number.");
                continue;
            }

            int playerChoice = scanner.nextInt();

            if (playerChoice == 0) {
                System.out.println("Goodbye!");
                break;
            }

            if (playerChoice < 1 || playerChoice > 3) {
                System.out.println("Invalid choice. Try again.");
                continue;
            }

            int computerChoice = 1 + random.nextInt(3);

            System.out.println("You chose:      " + choiceToString(playerChoice));
            System.out.println("Computer chose: " + choiceToString(computerChoice));

            int result = determineWinner(playerChoice, computerChoice);
            if (result == 0) {
                System.out.println("Result: It's a draw.");
            } else if (result == 1) {
                System.out.println("Result: You win!");
            } else {
                System.out.println("Result: Computer wins.");
            }
        }

        scanner.close();
    }
}
