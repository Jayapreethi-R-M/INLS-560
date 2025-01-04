#To import the random function from the library
import random

# To Define main function to play a new game of Black Jack.
def main():

    # To Call the function to get player's score.
    get_player_score()

    # Use while loop to ask the player if they want to play again.
    play_again = str(input("\nWould you like to play again? (y/n) "))
    while play_again == 'y':
        get_player_score()
        play_again = str(input("\nWould you like to play again? (y/n) "))

# To Define a function to get the player's score.
def get_player_score():

    # To Deal two cards to the player and print the sum of it.
    player_sum = deal_card() + deal_card()
    print("Your hand of two cards has a total value of " + str(player_sum) + ".")

    # To Prime the while loop to break the loop when needed.
    i = 0

    # To Ask user's choice to hit or stay until busted.
    while(player_sum <= 21) and (i == 0):
        extra_card = str(input("Would you like to take another card? (y/n) "))

        # Deal another card.
        if (extra_card == 'y'):
            player_sum = player_sum + deal_card()

            # Check if the player is busted.
            if (player_sum <= 21):
                print("Your hand now has a total value of " + str(player_sum) + ".")
            else:
                print("You BUSTED with a total value of " + str(player_sum) + "!")
                print("\n** You lose. **")

        # To not deal a card.
        else:
            print("You have stopped taking more cards with a hand value of " + str(player_sum) + ".")

            # Break the while loop.
            i = 1

            # Get the dealer's score
            dealer_score = get_dealer_score()

            # Check if the dealer is busted.
            if(dealer_score > 21):
                print("The dealer BUSTED with a value of " + str(dealer_score) + "!")
                print("\n** You win! **")
            else:
                print("The dealer was dealt a hand with a value of " + str(dealer_score) + ".")

                # To Check who won the game.
                if(dealer_score >= player_sum):
                    print("\n** You lose! **")
                else:
                    print("\n** You win! **")

# To Define function to randomly generate player's card.
def deal_card():
    player_card_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return (random.choice(player_card_deck))

# To Define a function to randomly generate dealer's card and making a sum.
def get_dealer_score():
    dealer_card_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealer_sum = (random.choice(dealer_card_deck) + random.choice(dealer_card_deck))

    # To Check if the dealer's hand is less than 16 and adding another card.
    while dealer_sum < 16:
        dealer_sum = dealer_sum + random.choice(dealer_card_deck)
    return dealer_sum

main()
