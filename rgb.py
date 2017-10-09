import Tkinter
import threading
import sys
from PIL import Image, ImageTk

points = []
#sudo apt-get install python-imaging-tk
def callback(event):
		print "clicked at: ", event.x, event.y
		points.append({'x':event.x,'y':event.y})
		if(len(points)>30):
			globals()['window'].destroy()

window = Tkinter.Tk(className="Image")
if __name__ == "__main__":
	if len(sys.argv) > 1:
		
		im = Image.open(sys.argv[1])
		canvas = Tkinter.Canvas(window, width=im.size[0], height=im.size[1])
		canvas.pack()
		image_tk = ImageTk.PhotoImage(im)
		canvas.create_image(im.size[0]//2, im.size[1]//2, image=image_tk)
		canvas.bind("<Button-1>", callback)
		Tkinter.mainloop()
		print points
		"""
		pic_thread = threading.Thread(target=create_image,args=(sys.argv[1],))
		pic_thread.start()
		window = Tkinter.Tk(className="bla")
		#im = Image.open(argv[1] if len(argv) >=2 else "bla2.png")
		 #Can be many different formats.
		canvas = Tkinter.Canvas(window, width=im.size[0], height=im.size[1])
		canvas.pack()
		image_tk = ImageTk.PhotoImage(im)
		canvas.create_image(im.size[0]//2, im.size[1]//2, image=image_tk)



		canvas.bind("<Button-1>", callback)
		Tkinter.mainloop()
		
		"""
		image = Image.open(sys.argv[1])
		pix = image.load()
		print image.size #Get the width and hight of the image for iterating over
		print pix[0,0] #Get the RGBA Value of the a pixel of an image
		#im.show()
	else:
		print "uso : {} <file>".format(sys.argv[0])







