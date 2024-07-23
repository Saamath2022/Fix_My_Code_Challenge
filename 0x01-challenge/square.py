class Square:
    def __init__(self, side_length):
        if side_length <= 0:
            raise ValueError("Side length must be positive")
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length
    
    def __str__(self):
        return f"Square(side_length={self.side_length})"
