import codecs as codecs
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
from collections import Counter

from matplotlib import style
style.use("ggplot")

"""
This is the Term Project for the course CP468 at Wilfrid Laurier Unviversity
Authors: Dhruv Sagar - 186802500
"""

"""
ASSUMPTIONS: We assume that the images of the signs are completely black and white in color
"""


# taking the images from dataset and converting it into numerical data for comparision.
def formingData():
    DataArrayExamples = open('numArEx.txt','a')
    DataRange = range(1,6)
    for Data in range(0,10):
        for extendedData in DataRange:

            imgFilePath = 'images/numbers/'+str(Data)+'.'+str(extendedData)+'.jpg'
            img = Image.open(imgFilePath)
            imgarr = np.array(img)
            imgli = str(imgarr.tolist())

            DataWrite = str(Data)+'::'+imgli+'\n'
            DataArrayExamples.write(DataWrite)

formingData()

def ASLnumrecogination(filePath):

    similarArr = []
    loadData = open('numArEx.txt','r').read()
    loadData = loadData.split('\n')
    image = Image.open(filePath)
    imagearr = np.array(image)
    imageli = imagearr.tolist()
    vari = str(imageli)
    for eachExample in loadData:
        # creating numerical data for the image being tested
        try:
            splitexample = eachExample.split('::')
            DataAvail = splitexample[0]
            ArrAvail = splitexample[1]
            PixelExample = ArrAvail.split('],')
            EachPixelData = vari.split('],')
            x = 0
            while x < len(PixelExample):
                # comparing the test image to the dataset
                if PixelExample[x] == EachPixelData[x]:
                    similarArr.append(int(DataAvail))

                x+=1
        except Exception as e:
            codecs.ignore_errors
            
                
    x = Counter(similarArr)
    print("Counters below show the pixels similarity of the test image to the dataset images.")
    print(x)
    plotX = []
    plotY = []

    for xyz in x:
        plotX.append(xyz)
        plotY.append(x[xyz])

    axis1 = plt.subplot2grid((4,4),(0,0), rowspan=1, colspan=4)
    axis2 = plt.subplot2grid((4,4),(1,0), rowspan=3,colspan=4)
    
    axis1.imshow(imagearr)
    axis2.bar(plotX,plotY,align='center')
    
    
    location = plt.MaxNLocator(12)
    axis2.xaxis.set_major_locator(location)

    #plotting the results as graphs for visual representation of the recogination.
    plt.show()

ASLnumrecogination('images/test0.jpg')
ASLnumrecogination('images/test1.jpg')
ASLnumrecogination('images/test2.jpg')
ASLnumrecogination('images/test3.jpg')
ASLnumrecogination('images/test4.jpg')
ASLnumrecogination('images/test5.jpg')
ASLnumrecogination('images/test6.jpg')
ASLnumrecogination('images/test7.jpg')
ASLnumrecogination('images/test8.jpg')
ASLnumrecogination('images/test9.jpg')