import os
import pytesseract
from PIL import Image
from collections import defaultdict

pytesseract.pytesseract.tesseract_cmd = 'tesseract.exe'


def get_max_pixel(image):
    '''
    获取图片中像素点数量最多的像素。
    '''

    pixel_dict = defaultdict(int)

    # 像素及该像素出现次数的字典
    width, height = image.size
    for i in range(width):
        for j in range(height):
            pixel = image.getpixel((i, j))
            pixel_dict[pixel] += 1
    # 求出最多的像素
    count_max = max(pixel_dict.values())
    pixel_dict_reverse = {v: k for k, v in pixel_dict.items()}
    return pixel_dict_reverse[count_max]


def get_bin_map(threshold):
    '''
    获取二值化映射。
    '''

    rate = 0.1  # 适当的比率。
    result = []
    for i in range(256):  # [0,255] 为像素可能值
        proper = threshold * (1 - rate) <= i <= threshold * (1 + rate)
        result.append(1 if proper else 0)
    return result


def denoise(image):
    '''
    降噪。
    '''

    width, height = image.size
    noise_position = []
    for i in range(1, width - 1):
        for j in range(1, height - 1):
            # 扫描像素为中点九宫格
            pixel_set = []
            for m in range(i - 1, i + 2):
                for n in range(j - 1, j + 2):
                    pixel = image.getpixel((m, n))
                    if pixel != 1:
                        pixel_set.append(pixel)
            # 如果黑色点小于 4 为噪点。
            if len(pixel_set) <= 4:
                noise_position.append((i, j))

    # 噪点设为黑色
    for position in noise_position:
        image.putpixel(position, 1)
    return image


def discern(image):
    '''
    识别。
    '''

    imgry = image.convert('L')  # 转为灰度图
    max_pixel = get_max_pixel(imgry)
    bin_map = get_bin_map(max_pixel)
    target = imgry.point(bin_map, '1')  # 二值化

    target = denoise(target)

    text = pytesseract.image_to_string(target)

    return text


def main():
    '''
    识别
    '''
    
    image = Image.open('assets/test.png')
    text = discern(image)
    print(text)


if __name__ == '__main__':
    main()
