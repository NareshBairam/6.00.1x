def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE (download ps4a.py to see)
    handlen = calculateHandlen(hand)
    total_score = 0
    #wordList = loadWords()
    while(handlen):
        print("Current Hand: ", end=" " )
        handList = displayHand(hand)
        Word = input("Enter word, or a '.' to indicate that you are finished: ") 
        if(Word == "."):
            print("Goodbye! Total score: %d points." % total_score) 
            break
        else:
            if(isValidWord(Word, hand, wordList)):
                total_score += getWordScore(Word, n) 
                hand = updateHand(hand, Word)
                handlen = calculateHandlen(hand)
                print("\" " + Word + " \"" + " earned " + str(getWordScore(Word, n)) + " points." + " Total: points " + str(total_score))
                print()
            else:
                print("Invalid word, please try again.")
                print()
            
    if(not handlen):    
        print("Run out of letters. Total score: %d points." % total_score)
        return