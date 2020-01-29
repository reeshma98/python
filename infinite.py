while True:
    ch = raw_input('Guess a number. (q) to quit ')
    if ch == 'q':
        break
    num = int(ch)
    if num > guess:
        print ' To high '
    elif num < guess:
        print ' To low '
    else:
        print ' Correct '
        break
