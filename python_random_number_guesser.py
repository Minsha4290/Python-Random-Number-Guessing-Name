import random

def play_guessing_game():
    while True:
        ANSWER = random.randint(0, 10)
        TRIES = 3

        print('\nWelcome! I have chosen a random number between 0 and 10.')
        print('You have', TRIES, 'tries to guess the number.')

        for tries in range(TRIES):
            guess = int(input('Enter your guess: '))
            if guess == ANSWER:
                print('You guessed correctly! You win!')
                break
            elif guess < ANSWER:
                print('Sorry, your answer is too low!')
                if tries < TRIES - 1:
                    print('You have', TRIES - tries - 1, 'tries left')
            elif guess > ANSWER:
                print('Sorry, your answer is too high!')
                if tries < TRIES - 1:
                    print('You have', TRIES - tries - 1, 'tries left.')
        else:
            print('Sorry you lost...the number was', ANSWER)

        play_again = input('Do you want to play again? (yes/no): ').lower()
        if play_again != 'yes':
            print('Goodbye!')
            break

play_guessing_game()
