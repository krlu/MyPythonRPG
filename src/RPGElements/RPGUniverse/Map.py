class GameMap(object):

    def __init__(self, dimensions):
        self.dimensions = dimensions
        
    
    def x_length(self):
        return self.dimensions[0]
        
    def y_length(self):
        return self.dimensions[1]

        