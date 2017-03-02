def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    newhand = hand.copy()
    if word in wordList:
        for i in word:
            if i in newhand and newhand[i] > 0:
                newhand[i] = newhand[i] - 1    
            else:
                return False
                
    else:
        return False
    return True
        
