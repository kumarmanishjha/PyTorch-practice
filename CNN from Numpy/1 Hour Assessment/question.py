"""
Author: Sanjay Thakur
"""

from PIL import Image
import numpy as np
from numpy import asarray


def your_answer(img, filterXX):
	"""Answer here"""
	    #Minmax normalization assuming 0 min and 255 max values
    imin = np.amin(image)
    imax = np.amax(image)
    img = (img - imin)/(imax - imin)
    
    
    #Convolution, assuming stride= filter size
    
    #Apply padding to image
    padding = 1
    img_padded = np.zeros((img.shape[0] + padding*2, img.shape[1] + padding*2)) #Create placeholder image with zero padding
    img_padded[int(padding):int(-1 * padding), int(padding):int(-1 * padding)] = image #Replace inner values with image
    #print(img_padded)
    
    #Convolution operation
    filter_size = filterXX.shape[0]
    stride = filter_size
    #Shape of feature maxp
    x_size = int(((img.shape[0] - filter_size + 2 * padding) / strides) + 1)
    y_size = int(((img.shape[1] - filter_size + 2 * padding) / strides) + 1)
    fmap = np.zeros((x_size, y_size))
    for y in range(img.shape[1]):
        if y > img.shape[1] - filter_size:
            break
        if y % stride == 0:
            for x in range(img.shape[0]):
                if x > img.shape[0] - filter_size:
                    break
                if x % strides == 0:
                    fmap[x, y] = (filterXX * img_padded[x: x + filter_size, y: y + filter_size]).sum()

    print('Feature map' +str(fmap))
    print('Feature map shape' +str(fmap.shape))
                    
    #Pooling
    pool_window = (2,2)
    pool_size = 2
    pool_out = np.zeros(np.int64((fmap.shape[0]-pool_size+1)/stride), np.int64((fmap.shape[1]-pool_size+1)/stride))
    for i in range(fmap.shape[-1]):
        row = 0
        for r in np.arange(0,fmap.shape[0]-pool_size-1, stride):
            col = 0
            for c in np.arange(0, fmap.shape[1]-pool_size-1, stride):
                pool_out[row, col,  i] = np.max([fmap[r:r+pool_size,  c:c+pool_size,  i]])
                col = col + 1
            row = row +1
            
    print('Pooling output' +str(pool_out))
    print('Pooled shape' +str(pool_out.shape))



if __name__ == "__main__":
	image = asarray(Image.open("image.jpg").convert('L'))
	filter33 = np.ones((3,3))
	your_answer(image, filter33)