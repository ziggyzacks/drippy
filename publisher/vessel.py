class Vessel:
    # using cm's
    def __init__(self, height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth

    @property
    def cross_section_area(self):
        return self.width * self.depth

    @property
    def total_volume(self):
        return self.cross_section_area * self.height
