'''
    CS5001 Spring2020
    Xue Wu 
    Project
    Class -- Score
'''


class Score:

    def __init__(self):

        self.score = 0

    def initialize_score(self, player):
        # Extract the total number winned by the player
        filename = player + '.txt'
        try:
            with open(filename, 'r') as infile:
                lines = infile.readlines()
                for char in lines:
                    return str(char)
        except OSError:
            try:
                # Initial new player score = 0
                with open(filename, 'w') as infile:
                    infile.write('0')
                    return '0'
            except OSError:
                print("Couldn't save your score.")
    
    def updated_score(self, player):
        # Update the total number winned by the player 
        filename = str(player) + '.txt'
        try:
            with open(filename, 'r')as infile:
                lines = infile.readlines()
                for char in lines:
                    self.score = int(char)
                self.score += 1
                try:
                    with open(filename, 'w')as infile:
                        infile.write(str(self.score))
                except OSError:
                    print('Could not save your score.')
        except OSError:
            print('Cannot read your file')
       
