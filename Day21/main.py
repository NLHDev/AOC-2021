class Player:
    def __init__(self, start_pos, name):

        self.playerName = name
        self.score = 0
        self.position = start_pos
        self.roll1 = 0
        self.roll2 = 0
        self.roll3 = 0
        self.movement = 0

    def check_win(self):
        if self.score >= 1000:
            print(self.playerName, " wins! Total rolls:", roll_counter)
            return True
        else:
            return False

    def roll_dice(self, roll):
        self.roll1 = roll
        self.roll2 = roll + 1
        self.roll3 = roll + 2

        if self.roll1 > 100:
            self.roll1 -= 100
        if self.roll2 > 100:
            self.roll2 -= 100
        if self.roll3 > 100:
            self.roll3 -= 100

        roll += 3
        if roll > 100:
            roll -= 100

        self.movement = self.roll1 + self.roll2 + self.roll3
        print(self.roll1, self.roll2, self.roll3, " = ", self.movement)
        return roll

    def move(self):
        self.position += self.movement
        while self.position > 10:
            self.position -= 10

        self.score += self.position
        print(self.playerName, " score: ", self.score, "Position: ", self.position)


# ---------- MAIN ------------ #
if __name__ == '__main__':
    roll_counter = 0
    p1 = Player(4, 'Player1')
    p2 = Player(9, 'Player2')
    roll = 1

    # Main Game Loop
    while not p1.check_win() and not p2.check_win():
        roll = p1.roll_dice(roll)
        p1.move()
        roll_counter += 3
        if p1.check_win():
            print("Losing Player Score: ", p2.score)
            print(roll_counter * p2.score)
            break

        roll = p2.roll_dice(roll)
        p2.move()
        roll_counter += 3
        if p2.check_win():
            print("Losing Player Score: ", p1.score)
            print(roll_counter * p1.score)
            break

exit()