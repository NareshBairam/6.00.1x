
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    alphabets = list(alphabets)
    for i in lettersGuessed:
        if(i in alphabets):
            alphabets.remove(i)
    alphabets = ''.join(alphabets)
    return alphabets
