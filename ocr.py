import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def readTextFromImg(img: str):
    img = cv2.imread(img)
    img_convert = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # cv2.imshow('image', img_convert)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    print(pytesseract.image_to_string(img_convert))