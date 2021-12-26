from PIL import Image
import os,sys

def wa():
    image1 = Image.open(r'./pic.jpg')
    im1 = image1.convert('RGB')
    im1.save(r'./myFirstImage.pdf')

    from fpdf import FPDF
    pdf = FPDF()
    # imagelist is the list with all image filenames

    image='./pic.jpg'
    pdf.add_page()
    pdf.image(image)
    pdf.output("yourfile.pdf", "F")


ALLOWED_EXTENSIONS=set(['jpg'])
def ispic(filename):
    print('.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS)

ispic("wa.jpg")