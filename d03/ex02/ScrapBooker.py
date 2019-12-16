import numpy as np

class ScrapBooker:

    def crop(array, dimensions, position=(0,0)):
        try:
            assert dimensions[0] > array.shape[0] or dimensions[1] > array.shape[1]
            array.resize(dimensions)
            
            return (array)
        except:
            print('ERROR CROP')
    def thin(array, n, axis):

    def juxtapose(array, n, axis):

    def mosaic(array, dimensions):
