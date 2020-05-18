class Board:
    def __init__(self, state=None):
        self.state = state

    def draw(self):
        result = ''
        for y in range(3):
            for x in range(3):
                if (x, y) == self.state:
                    result += 'X'
                else:
                    result += '.'
            result += '\n'
        return result.strip()

    def take_turn(self, x, y):
        return Board((x, y))

