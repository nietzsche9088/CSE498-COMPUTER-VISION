#Terminal command
##cd /cv_ass1/src 
##python main.py
######Task1 Image Sharpening
I choose Guassian kernel here and the kernel size is defaulted to 3, sigma is set to 2.0. After operations, images 1.jpg *before and after* are as follows. 

![before](/data/task1/1.jpg)
![after](/output/task1/enhanced_1.jpg)
**CSE 498 Question**
From Task1, there're 2 steps. First, let original signal substract lowpass signal then add back original signal. Laplacian sharpening is one method that can sharpen the image in one step. Compute Laplacian mask and convolve with original image. Laplacian operator is a derivate operator so it highlights gray-level discontinuities in an image and deemphasizes regions with slowly varying gray levels. Also, it tends to produce images that have grayish edge lines and other discontinuities and featureless background.

######Task2 Image Denoising
I implement three filtering techniques individually and here's one example output.
![original image](/data/task2/sp_image1.jpg)
![Mean Filter](/output/task2/Mean_sp_image1.jpg)
![Guassian Filter](/output/task2/Gaussian_sp_image1.jpg)
![Median Filter](/output/task2/Median_sp_image1.jpg)

**Analysis**
For each image, Median filtering works best because it don't count on the edge elements. That's why it smoothes. 

The bigger size of the kernel, the time running the function increases except certain point.
![size_time_relation](/output/task2/Size_time.jpg)
######Task3 Sobel Filtering
In this task, I implement the horizontal and vertical sobel kernel seperately. Then combine the two to display magnitude.
![horizontal](/output/task2/horizontal_lehigh1.jpeg)
![vertical](/output/task2/vertical_lehigh1.jpeg)
![magnitude](/output/task2/magnitude_lehigh1.jpeg)
**CSE 498 Question**
Edge orientation helps outline and distinguish the two ares with large contrast ratios.

######References
[Unsharp filter](https://homepages.inf.ed.ac.uk/rbf/HIPR2/unsharp.htm)
[Lecture Sharpening](https://bohr.wlu.ca/hfan/cp467/12/notes/cp467_12_lecture6_sharpening.pdf)
[Edge Detection](https://www.cs.auckland.ac.nz/compsci373s1c/PatricesLectures/Edge%20detection-Sobel_2up.pdf)
[Gradients and Edge Detection](http://www.cse.psu.edu/~rtc12/CSE486/lecture05.pdf)