#Painting Scatter Plot (Styles)
#@Diana Kim June.01.2021
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage,AnnotationBbox)
from matplotlib.lines import Line2D

# color mapping to styles
def color_map(idx):
    print(idx)
    colors_={'Abstract_Expressionism':'red','Action_painting':'orange','Analytical_Cubism':'yellow','Cubism':'greenyellow','Expressionism':'green','Fauvism':'deepskyblue','Impressionism':'slateblue','Minimalism':'magenta','Pop_Art':'gray','Post_Impressionism':'black','Synthetic_Cubism':'darkcyan'}
    return colors_[idx]

#########Please change the path/File name 
df=pd.read_csv("example.csv",header=0)
df['color']=df['art_style'].apply(color_map)
embedding_=np.load("embedding_random.npz") #load embeddings ['embedding']
data_=embedding_['embedding']
img_path="./imgs/"# path for images
painting_hold=True # holding or disapperaing  as a new point is pressed (False:disappear) 



class Visual_2D:                                                                                                                                                           
    def __init__(self,data,painting_hold):
        self.data_=data
        self.hold_annotation=painting_hold
        self.fig,self.ax=plt.subplots()
        self.scatter_()
        self.cid=self.fig.canvas.mpl_connect('pick_event',self)
        self.anno_box=[]

    def scatter_(self):
        colors_=['red','orange','yellow','greenyellow','green','deepskyblue','slateblue','magenta','gray','black','darkcyan']
        labels = ['Abstract_Expressionism','Action_painting','Analytical_Cubism','Cubism','Expressionism','Fauvism','Impressionism','Minimalism','Pop_Art','Post_Impressionism','Synthetic_Cubism']
        for c in colors_:
            lines = [Line2D([0], [0], marker='o', color=c,markersize=10) for c in colors_]
        self.ax.scatter(self.data_[:,0],self.data_[:,1],c=df['color'],s=2,picker=4)
        self.ax.legend(lines, labels)

    def __call__(self,event):


        if self.hold_annotation is False: #holding or delelete  as a new point is pressed (False:disappear)
            if self.anno_box: 
                self.anno_box[0].remove()
                self.anno_box.clear()
                print("removed!")
        
        idx_=event.ind[0] #index of points to be pressed. (as mulple points are ovelapped a point is indicated by [0])
        xy=(self.data_[idx_,0],self.data_[idx_,1]) # axis of (x,y)

        painting_=df.iloc[[idx_]]['painting'].values[0]#painting
        style_=df.iloc[[idx_]]['art_style'].values[0]#style        
        path_=img_path+style_+"/"+painting_+".jpg"
        arr_img = plt.imread(path_)
        imagebox = OffsetImage(arr_img,zoom=0.035) #zoom controls image size
        ab = AnnotationBbox(imagebox,xy,xycoords='data')
        self.anno_box.append(ab)
        self.ax.add_artist(ab)
        ab.set_visible(True)
        self.fig.canvas.draw_idle()


def color_map(idx):
    print(idx)
    colors_=['red','orange','yellow','greenyellow','green','deepskyblue','slateblue','magenta','gray',]
    return colors_[idx]
    
    
def main():
    embedding_=np.load("embedding_random.npz") #load embeddings ['embedding']
    data_=embedding_['embedding']
    graph_=Visual_2D(data_,painting_hold)#draw scatter plot and receive user event
    plt.show()
                                                                                                                                                                           
if __name__ == "__main__":                                                                                                                                                 
    main()                                                                                                                                                             

        
