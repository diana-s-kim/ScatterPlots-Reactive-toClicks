<h3 align="center">Displayinig Corresponding Images by Clicking Data Points</h3>
<div align="left">
This python code is written while working on art-data analysis projects.<br>
The code reads and displays the images corresponding to 2-D data points clicked by users. <br>
By doing so, it helps to understand the relationship between the images and data points' geometry. <br>
The example figure below presents 110 two-dimensional data samples with different colors based on their styles. <br>

<div align="center">
<figure style="width: 50%; font-style: itlaic; font-size: smaller text-align: center;">
<img src="example.png" width=550 height=430><br/>
<figcaption>Figure: six corresponding paintings are shown as six arbitrary data points are clicked.</figcaption>
</figure>
</div>
</br>


<h4>&#x25BA; Files</h4>
<ol>
<li> Run: python color_visualization.py
<li> Data embedding (110 random points): embedding_random.npz
<li> Image meta information: example.csv
<li> Images: ./imgs/
<li> User Display Option: painting_hold=True (previous images are hold when new data points are clicked.)
</ol>

&#42;&#42;The order of data points in the embedding must correspond to the order of meta information&#42;&#42;