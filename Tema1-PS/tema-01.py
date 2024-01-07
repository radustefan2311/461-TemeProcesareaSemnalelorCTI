# Codreanu Radu Stefan - 461
# Tema 1 - Algoritmul JPEG - Procesarea semnalelor

import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy.fft import dctn, idctn
from skimage import color

X = misc.ascent()
plt.imshow(X)
plt.show()

# Matricea de cuantizare (Q_jpeg):
Q_jpeg = [[16, 11, 10, 16, 24, 40, 51, 61],
        [12, 12, 14, 19, 26, 28, 60, 55],
        [14, 13, 16, 24, 40, 57, 69, 56],
        [14, 17, 22, 29, 51, 87, 80, 62],
        [18, 22, 37, 56, 68, 109, 103, 77],
        [24, 35, 55, 64, 81, 104, 113, 92],
        [49, 64, 78, 87, 103, 121, 120, 101],
        [72, 92, 95, 98, 112, 100, 103, 99]]


def sub_a():
    blocks = [] # inițializam o listă goală numită blocks pentru a stoca blocurile de imagini comprimate.
    rows = X.shape[0]
    columns = X.shape[1]

    for i in range(0, rows, 8):
        for j in range(0, columns, 8):
            block = X[i : i + 8, j : j + 8] # Aceasta extrage un bloc de 8x8 din imaginea originală.
            y = dctn(block)
            y_jpeg = Q_jpeg * np.round(y/Q_jpeg)
            x_jpeg = idctn(y_jpeg)
            blocks.append(x_jpeg)

    block_size = X.shape[1] // 8 # Extragem dimensiunea blocului 
    blocks = [X[:, i : i + block_size] for i in range(0, X.shape[1], block_size)] # Cream blocuri facand un slice pe X cu dimensiunea blocului
    compressed_image = np.block(blocks) # Concatenam blocurile de-a lungul axei orizontale pentru a crea imaginea comprimată

    plt.subplot(1, 2, 1)
    plt.imshow(X, cmap=plt.cm.gray)
    plt.title('Imaginea originala')

    plt.subplot(1, 2, 2)
    plt.imshow(compressed_image, cmap=plt.cm.gray)
    plt.title('Imaginea JPEG')

    plt.show()

def sub_b_2():
    X_rgb = misc.face()
    X_ycbcr = color.rgb2ycbcr(X_rgb) # X_ycbcr este creat prin conversia imaginii RGB în spațiul de culoare YCbCr folosind color.rgb2ycbcr().

    # Matrice de cuantizare pentru componenta Y:
    Q_jpeg_Y = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                        [12, 12, 14, 19, 26, 28, 60, 55],
                        [14, 13, 16, 24, 40, 57, 69, 56],
                        [14, 17, 22, 29, 51, 87, 80, 62],
                        [18, 22, 37, 56, 68, 109, 103, 77],
                        [24, 35, 55, 64, 81, 104, 113, 92],
                        [49, 64, 78, 87, 103, 121, 120, 101],
                        [72, 92, 95, 98, 112, 100, 103, 99]])

    # Matrice de cuantizare pentru componentele Cb și Cr:
    Q_jpeg_CbCr = np.array([[17, 18, 24, 47, 99, 99, 99, 99],
                            [18, 21, 26, 66, 99, 99, 99, 99],
                            [24, 26, 56, 99, 99, 99, 99, 99],
                            [47, 66, 99, 99, 99, 99, 99, 99],
                            [99, 99, 99, 99, 99, 99, 99, 99],
                            [99, 99, 99, 99, 99, 99, 99, 99],
                            [99, 99, 99, 99, 99, 99, 99, 99],
                            [99, 99, 99, 99, 99, 99, 99, 99]])

    # Lista blocurilor comprimate pentru fiecare canal de culoare
    compressed_blocks_Y = []
    compressed_blocks_Cb = []
    compressed_blocks_Cr = []

    # Un for pentru fiecare canal de culoare
    for channel in range(X_ycbcr.shape[2]):
        # Alegem matricea in functie de canal
        Q_matrix = Q_jpeg_Y if channel == 0 else Q_jpeg_CbCr
        compressed_blocks_channel = []
        
        for i in range(0, X_ycbcr.shape[0], 8):
            for j in range(0, X_ycbcr.shape[1], 8):
                block = X_ycbcr[i : i + 8, j : j + 8, channel]
                y = dctn(block)
                y_jpeg = Q_matrix * np.round(y / Q_matrix)
                x_jpeg = idctn(y_jpeg)
                compressed_blocks_channel.append(x_jpeg)

        if channel == 0:
            compressed_blocks_Y = compressed_blocks_channel
        else:
            if channel == 1:
                compressed_blocks_Cb = compressed_blocks_channel
            else:
                compressed_blocks_Cr = compressed_blocks_channel

    # Combinam componentele Y, Cb și Cr pentru a obține imaginea YCbCr comprimată
    block_size = X_ycbcr.shape[1] // 8
    # Construim imaginea comprimată pentru canalul de luminanță (Y).
    compressed_image_Y = np.block([compressed_blocks_Y[i : i + block_size] for i in range(0, len(compressed_blocks_Y), block_size)])
    # În mod similar, construim imaginea comprimată pentru canalul de crominanță (Cb).
    compressed_image_Cb = np.block([compressed_blocks_Cb[i : i + block_size] for i in range(0, len(compressed_blocks_Cb), block_size)])
    # Această linie construiește imaginea comprimată pentru canalul de crominanță (Cr).
    compressed_image_Cr = np.block([compressed_blocks_Cr[i : i + block_size] for i in range(0, len(compressed_blocks_Cr), block_size)])

    # Combinam componentele Y, Cb și Cr pentru a obține imaginea YCbCr comprimată
    compressed_image = np.stack([compressed_image_Y, compressed_image_Cb, compressed_image_Cr], axis=2)

    plt.subplot(1, 2, 1)
    plt.imshow(X_rgb)
    plt.title('Imaginea originala')

    plt.subplot(1, 2, 2)
    plt.imshow(color.ycbcr2rgb(compressed_image))
    plt.title('Imaginea JPEG')

    plt.show()

def mse_calc(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    return mse

def sub_c(X, Q_jpeg, mse_limit):
    rows, columns = X.shape
    blocks = []
    
    for i in range(0, rows, 8):
        for j in range(0, columns, 8):
            block = X[i : i + 8, j : j + 8]
            y = dctn(block)
            y_jpeg = Q_jpeg * np.round(y/Q_jpeg)
            x_jpeg = idctn(y_jpeg)
            blocks.append(x_jpeg)

    compressed_image = np.block([blocks[i : i + columns // 8] for i in range(0, len(blocks), columns // 8)])

    mse = mse_calc(X, compressed_image)

    while mse > mse_limit:
        # Ștergem lista de blocuri înainte de a o reutiliza
        blocks = []
        
        # Continuam să comprimam imaginea până când MSE este sub prag
        for i in range(0, rows, 8):
            for j in range(0, columns, 8):
                block = compressed_image[i : i + 8, j : j + 8]
                y = dctn(block)
                y_jpeg = Q_jpeg * np.round(y/Q_jpeg)
                x_jpeg = idctn(y_jpeg)
                blocks.append(x_jpeg)

        compressed_image = np.block([blocks[i : i + columns // 8] for i in range(0, len(blocks), columns // 8)])
        mse = mse_calc(X, compressed_image)

    plt.subplot(1, 2, 1)
    plt.imshow(X, cmap=plt.cm.gray)
    plt.title('Imaginea originala')

    plt.subplot(1, 2, 2)
    plt.imshow(compressed_image, cmap=plt.cm.gray)
    plt.title('Imaginea JPEG')

    plt.show()

sub_c(X,Q_jpeg, 100)