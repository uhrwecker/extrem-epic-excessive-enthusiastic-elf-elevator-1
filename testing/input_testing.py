"""testing inputs so you dont throw shit in the programm"""

def test_string(string, expection):
    """tests user inputs, maybe not needed in final version
    arg:
        string: the input that needs to be tested
        expection: the input it should be"""
    
    if expection == 'name':
        lenght = len(string)
        if lenght == 0:
            print("You made no input.")
            return False
        if lenght <= 15:
            return True
        if lenght > 15:
            print("Your input is to long.")
            return False
        
    if expection == 'race':
        races = ['human', 'orc']
        if string in races:
            return True
        else:
            print("Your input wasnt correct.")
            return False
        
    if expection == 'alignment':
        alignments = ['fighter', 'mage']
        if string in alignments:
            return True
        else:
            print("Your input wasnt correct.")
            return False