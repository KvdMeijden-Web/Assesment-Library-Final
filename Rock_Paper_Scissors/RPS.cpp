#include <iostream>
#include <cstdlib>
#include <ctime>

int determineWinner(int player, int computer) {
    if (player == computer) return 0;        // draw
    if ((player == 1 && computer == 3) ||    // rock beats scissors
        (player == 2 && computer == 1) ||    // paper beats rock
        (player == 3 && computer == 2)) {    // scissors beats paper
        return 1;                            // player wins
    }
    return -1;                               // computer wins
}

std::string choiceToString(int choice) {
    switch (choice) {
        case 1: return "Rock";
        case 2: return "Paper";
        case 3: return "Scissors";
        default: return "Unknown";
    }
}

int main() {
    std::srand(static_cast<unsigned int>(std::time(nullptr)));

    std::cout << "Rock-Paper-Scissors (C++)\n";

    while (true) {
        std::cout << "\n1) Rock  2) Paper  3) Scissors  0) Quit\n";
        std::cout << "Your choice: ";

        int playerChoice;
        if (!(std::cin >> playerChoice)) {
            std::cin.clear();
            std::cin.ignore(10000, '\n');
            std::cout << "Invalid input. Please enter a number.\n";
            continue;
        }

        if (playerChoice == 0) {
            std::cout << "Goodbye!\n";
            break;
        }

        if (playerChoice < 1 || playerChoice > 3) {
            std::cout << "Invalid choice. Try again.\n";
            continue;
        }

        int computerChoice = 1 + std::rand() % 3;

        std::cout << "You chose:      " << choiceToString(playerChoice) << "\n";
        std::cout << "Computer chose: " << choiceToString(computerChoice) << "\n";

        int result = determineWinner(playerChoice, computerChoice);
        if (result == 0) {
            std::cout << "Result: It's a draw.\n";
        } else if (result == 1) {
            std::cout << "Result: You win!\n";
        } else {
            std::cout << "Result: Computer wins.\n";
        }
    }

    return 0;
}
