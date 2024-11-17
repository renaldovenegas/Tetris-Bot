from abc import ABC, abstractmethod

class BasePiece(ABC):
    @abstractmethod
    def rotate(self, num_times):
        pass

    def get_shape(self): 
        pass

    def get_num_rows(self): 
        pass

    def get_num_cols(self): 
        pass


class PieceL(BasePiece): 
    def __init__(self):
        self.orientations = [
                            [[1, 0], 
                             [1, 0], 
                             [1, 1]],
                            [[1, 1, 1], 
                             [1, 0, 0]], 
                            [[1, 1], 
                             [0, 1], 
                             [0, 1]], 
                            [[0, 0, 1], 
                             [1, 1, 1]]
                            ]
        self.num_orientations = 4
        self.current_index = 0
        self.current_orientation = self.orientations[0]
        self.num_rows = len(self.current_orientation)
        self.num_cols = len(self.current_orientation[0])
        self.top_left = (0, 0) #x and y of top left corner, defaults 0, 0 

    def rotate(self, num_times): 
        self.current_index = (self.current_index + num_times) % self.num_orientations
        self.current_orientation = self.orientations[self.current_index]
        self.num_rows = len(self.current_orientation)
        self.num_cols = len(self.current_orientation[0]) 

    def get_shape(self): 
        return self.current_orientation
    
    def get_num_rows(self): 
        return self.num_rows
    
    def get_num_cols(self): 
        return self.num_cols

    def set_location(self, x, y): 
        self.top_left = (x, y)

    def get_location(self): 
        return self.top_left


class PieceI(BasePiece): 
    def __init__(self):
        self.orientations = [
                            [[1], 
                             [1], 
                             [1], 
                             [1]], 
                            [[1,1,1,1]]
                            ]
        self.num_orientations = 2
        self.current_index = 0
        self.current_orientation = self.orientations[0]
        self.num_rows = len(self.current_orientation)
        self.num_cols = len(self.current_orientation[0])
        self.top_left = (0, 0) #x and y of top left corner, defaults 0, 0 

    def rotate(self, num_times): 
        self.current_index = (self.current_index + num_times) % self.num_orientations
        self.current_orientation = self.orientations[self.current_index]
        self.num_rows = len(self.current_orientation)
        self.num_cols = len(self.current_orientation[0]) 

    def get_shape(self): 
        return self.current_orientation
    
    def get_num_rows(self): 
        return self.num_rows
    
    def get_num_cols(self): 
        return self.num_cols

    def set_location(self, x, y): 
        self.top_left = (x, y)

    def get_location(self): 
        return self.top_left

class PieceO(BasePiece): 
    def __init__(self):
        self.orientations = [
                            [[1,1], 
                             [1,1]]
                            ]
        self.num_orientations = 1
        self.current_index = 0
        self.current_orientation = self.orientations[0]
        self.num_rows = len(self.current_orientation)
        self.num_cols = len(self.current_orientation[0])
        self.top_left = (0, 0) #x and y of top left corner, defaults 0, 0 

    def rotate(self, num_times): 
        self.current_index = (self.current_index + num_times) % self.num_orientations
        self.current_orientation = self.orientations[self.current_index]
        self.num_rows = len(self.current_orientation)
        self.num_cols = len(self.current_orientation[0]) 

    def get_shape(self): 
        return self.current_orientation
    
    def get_num_rows(self): 
        return self.num_rows
    
    def get_num_cols(self): 
        return self.num_cols

    def set_location(self, x, y): 
        self.top_left = (x, y)

    def get_location(self): 
        return self.top_left


class PieceJ(BasePiece): 
    def __init__(self):
        self.orientations = [
                            [[0,1], 
                             [0,1], 
                             [1,1]], 
                            [[1, 0, 0], 
                             [1, 1, 1]], 
                            [[1, 1], 
                             [1, 0], 
                             [1, 0]], 
                            [[1, 1, 1], 
                             [0, 0, 1]]]
        self.num_orientations = 4
        self.current_index = 0
        self.current_orientation = self.orientations[0]
        self.num_rows = len(self.current_orientation)
        self.num_cols = len(self.current_orientation[0])
        self.top_left = (0, 0) #x and y of top left corner, defaults 0, 0 

    def rotate(self, num_times): 
        self.current_index = (self.current_index + num_times) % self.num_orientations
        self.current_orientation = self.orientations[self.current_index]
        self.num_rows = len(self.current_orientation)
        self.num_cols = len(self.current_orientation[0]) 

    def get_shape(self): 
        return self.current_orientation
    
    def get_num_rows(self): 
        return self.num_rows
    
    def get_num_cols(self): 
        return self.num_cols

    def set_location(self, x, y): 
        self.top_left = (x, y)

    def get_location(self): 
        return self.top_left