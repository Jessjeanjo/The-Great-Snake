

def sleep_in(weekday, vacation):
    '''
    The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
    We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in. '''
    if weekday == False and (vacation == True or vacation == False):
        return True
    elif weekday == True and vacation == False:
        return False
    elif weekday == True and vacation == True:
        return True

