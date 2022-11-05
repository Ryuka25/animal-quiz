NUMBER_OF_ATTEMPT = 3

def main():
    global score 
    score = 0
    print('Gues the Animal!')
    
    guess_1 = input('Which bear lives at the North Pole? ')
    check_guess(guess_1, 'polar bear')
    
    guess_2 = input('Which is the fastest land animal? ')
    check_guess(guess_2, 'cheetah')
    
    guess_3 = input('Which is the largest animal? ')
    check_guess(guess_3, 'blue whale')
    
    guess_4 = input('Which one of these is a fish?\n' \
                    ' A) Whale\n B) Dolphin\n C) Shark\n D) Squid\n' \
                    'Type A, B, C or D ')
    check_guess(guess_4, 'C')
    
    guess_5 = input('Mice ar mammals. True or False? ')
    check_guess(guess_5, 'True')
    
    print('Your score is ' + str(score))
 
def check_guess(guess, answer):
    global score
        
    still_guessing = True
    attempt = 0
    
    while (still_guessing and attempt < NUMBER_OF_ATTEMPT):
        if (guess.lower() == answer.lower()):
            print('Correct answer')
            max_score_to_add = 3
            score += (max_score_to_add - attempt)
            still_guessing = False
        else:
            if (attempt < (NUMBER_OF_ATTEMPT - 2)):
                guess = input('Sorry wrong asnwer. Try again. ')
            attempt += 1
        
    if (attempt == NUMBER_OF_ATTEMPT):
        print('The correct answer is ' + answer)

if (__name__ == '__main__'):
    main()