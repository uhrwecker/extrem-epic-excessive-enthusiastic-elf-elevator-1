"""contains functions to test player inputs"""

def test_string(string, expection):
    
    if expection == 'race':
        races = ['human', 'orc']
        if string in races:
            return True
        else:
            return False
        

