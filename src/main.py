from user_prompt import get_keylist, select_difficulty, select_random_key, key_to_art

def main():
    print("Welcome to type-it! Press the correct key/button when prompted to score.\n")
    difficulty = select_difficulty()
    keylist = get_keylist(difficulty)
    print(keylist)
    key = select_random_key(difficulty)
    print(key)
    ascii_key = key_to_art(key)
    print(ascii_key)
#TODO:use library to make ascii gen function - maybe art? on pypi
    # open window
    # prompt user to start
    #display high_score
    # set current_score to 0
    # countdown
    # start song/ticking noise
    # audio prompt
    # visual prompt

    # success = True
    # while success == True:
    #     success = False
    #     present_prompt()
    #     await_input()
    #     start_timer()
    #     if success:
    #         speed_up()
    #     else:
    #         game_over()
              # if highscore ask for name and change highscore variable
    #         reset()
    #         retry = try_again()
    #         if retry:
    #               score = 0
    #               speed = 1
    #           else:
    #               quit
    #
    #     ^^maybe one of these returns a bool to decide if success or failure. maybe combine.
    # maybe whole thing can be an infinite loop that breaks when try again = no


if __name__ == "__main__":
    main()
