import os
folder = os.getcwd()
imgPath = os.path.join(folder, 'RoboFabDocs.roboFontExt/lib/images/logo.gif')
size(512, 512)
fill(1)
rect(0, 0, width(), height())
scale(4.1)
image(imgPath, (11, 17))
saveImage(os.path.join(folder, 'roboFabDocsMechanicIcon.png'))
