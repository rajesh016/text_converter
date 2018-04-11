import Image ,ImageEnchance
def main():
    filename = 'file.jpeg'
    image = Image.open(filename)
    size = width,height =image.size

    enhancer = ImageEnchance.Brightness( image )

    image=enhancer.Sharpness(2.0)

    image.save("modified_"+filename)
    del image


if(__name__=="__main__"):
    main()