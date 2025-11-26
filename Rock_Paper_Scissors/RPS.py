import random

def determine_winner(player, computer):
    if player == computer:
        return 0  # draw
    if ((player == 1 and computer == 3) or  # rock beats scissors
        (player == 2 and computer == 1) or  # paper beats rock
        (player == 3 and computer == 2)):   # scissors beats paper
        return 1  # player wins
    return -1     # computer wins


def choice_to_string(choice):
    if choice == 1:
        return "Rock"
    if choice == 2:
        return "Paper"
    if choice == 3:
        return "Scissors"
    return "Unknown"


def main():
    print("Rock-Paper-Scissors (Python)")

    while True:
        print("\n1) Rock  2) Paper  3) Scissors  0) Quit")
        choice_str = input("Your choice: ")

        if not choice_str.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        player_choice = int(choice_str)

        if player_choice == 0:
            print("Goodbye!")
            break

        if player_choice not in (1, 2, 3):
            print("Invalid choice. Try again.")
            continue

        computer_choice = random.randint(1, 3)

        print("You chose:     ", choice_to_string(player_choice))
        print("Computer chose:", choice_to_string(computer_choice))

        result = determine_winner(player_choice, computer_choice)
        if result == 0:
            print("Result: It's a draw.")
        elif result == 1:
            print("Result: You win!")
        else:
            print("Result: Computer wins.")


if __name__ == "__main__":
    main()
