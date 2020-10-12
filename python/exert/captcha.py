import random
from PIL import Image, ImageFont, ImageDraw


class Captcha:
    '''
    '''

    def __init__(self, font_size=50):
        '''
        '''
        self.font_size = font_size
        self.font = ImageFont.truetype(
            font='assets/source-han-serif-cn-bold.ttf',
            size=font_size
        )

    def make(self, text):
        '''
        '''

        length = len(text)
        height = self.font_size * 2
        width = length * height
        size = (width, height)
        image = Image.new(mode="RGBA", size=size)
        for i in range(length):
            left = int(self.font_size * 0.3 + i * random.randint(80, 90))
            code = text[i]
            item = self.draw(code)
            temp = Image.new(mode="RGBA", size=size)
            temp.paste(item, box=(left, 0))
            image = Image.alpha_composite(image, temp)
        return image

    def save(self, text, path):
        with open(path, 'wb') as writer:
            image = self.make(text)
            image.save(writer)

    def draw(self, code):
        '''
        '''

        size = (self.font_size * 2, self.font_size * 2)
        image = Image.new(mode="RGBA", size=size)
        draw = ImageDraw.Draw(image)
        position = (int(self.font_size * 0.6), int(self.font_size * 0.1))
        draw.text(position, code, font=self.font)
        angle = random.randint(-50, 50)
        return image.rotate(angle, expand=1, resample=Image.BILINEAR)

captcha = Captcha()
captcha.save('12fg34', 'a.png')
