from tkinter import Tk, Canvas, Frame, Menu, BOTH, filedialog
from parse import Parser
from graphics import PythonGraphics, SVGGraphics
import svgwrite

class ShapeDrawing(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.widgets()
        self.shapes = []

    def widgets(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.onOpen)
        fileMenu.add_command(label="Clear", command=self.onClear)
        fileMenu.add_command(label="Export", command=self.onExport)
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)

        self.master.title("Shape Drawing")
        self.pack(fill=BOTH, expand=1)

        self.canvas = Canvas(self)
        self.canvas.pack(fill=BOTH, expand=1)

    def onOpen(self):
        # display an open file dialog
        file = filedialog.askopenfilename(title="Select file", filetypes = [('JSON File', '*.json'),('All Files', '*.*')], defaultextension = ('JSON File', '*.json'))

        #return if no file selected
        if not file:
            return

        # read shapes from the json file
        parser = Parser()
        self.shapes = parser.parse_shapes(file)

        #clear the canvas
        self.canvas.delete("all")

        #create a python graphics instance
        graphics = PythonGraphics()
        graphics.drawlocation = self.canvas

        #draw the shapes using the python graphics
        for shape in self.shapes:
            shape.draw(graphics)

    def onClear(self):
        self.canvas.delete("all")
        self.shapes = []

    def onExport(self):

        #display a save file dialog
        file = filedialog.asksaveasfile(mode='w', filetypes = [('SVG File', '*.svg'),('All Files', '*.*')], defaultextension = ('SVG File', '*.svg'))

        if not file:
            return
        
        #create an SVG graphics instance
        graphics = SVGGraphics()
        svgfile = svgwrite.Drawing()
        graphics.drawlocation = svgfile

        # draw the shapes using the svg graphics
        for shape in self.shapes:
            shape.draw(graphics)
        
        # write the drawn svg graphics to the chosen file and close the file
        file.write(svgfile.tostring())
        file.close()
    

    def onExit(self):
        self.quit()

def main():

    root = Tk()
    root.title("Shape Drawing")
    root.geometry("400x250+300+300")
    app = ShapeDrawing(root)

    root.mainloop()


if __name__ == '__main__':
    main()
