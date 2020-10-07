# [exert-tesseract-ocr](https://github.com/chaosannals/exert-tesseract-ocr)

命令行得出识别结果。

```bash
tesseract test.png output -l eng
```

由于 tesseract 的识别很有限，所以图片在识别前最好先处理过。
比如 python 利用 pillow 处理后在由 tesseract 识别会好些。

## 训练

提高识别率还可以训练 tesseract 来提高。
