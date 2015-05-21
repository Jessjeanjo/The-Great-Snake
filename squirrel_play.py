def squirrel_play(temp, is_summer):
    '''The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is
    between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90.
    Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise. '''
    if is_summer == True:
        if 60 <= temp <= 100:
            return True
        else:
            return False
    else:
        if 60 <= temp <= 90:
            return True
        else:
            return False



