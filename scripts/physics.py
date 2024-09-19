# In physics.py

class Physics:
    def __init__(self):
        self.vel = 0
        self.rect = None

    def gravity(self):
        self.vel += 0.5
        if self.vel > 7:
            self.vel = 7
        if self.rect:
            self.rect.y += int(self.vel)