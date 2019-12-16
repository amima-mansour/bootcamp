import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class ImageProcessor:

    def load(path):
        img = mpimg.imread(path)
        print('Loading image of dimensions {} x {}'.format(img.shape[0], img.shape[1]))
        return img

    def display(array):
        imgplot = plt.imshow(array)
        #plt.show()
        return imgplot