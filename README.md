# Face Detection Examples 

Basic tutorials/examples depicting the performance, accuracy and other characteristics of a couple of face detection technologies. Very loosely based on a demo for a client related to the face detection technology their current solution was using vs. the new solution we suggested they go with. 


### Update History

* **07/19/2022:** 
* Updated the initial set of examples with another example using MobileNet SSD running on OpenCV's DNN module
* Added information to download the model and weights files for both Haar Cascade and MobileNet SSD  

* **4/21/2022:** initial commit with examples of facial detection using Haar Cascade with OpenCV and MTCNN, including external helper scripts for the Jupyter Notebook, and sample image files  

### Note on images
* The images used in this repo are either just images I found online or come from the [Labeled Faces in the Wild Dataset.](http://vis-www.cs.umass.edu/lfw/) If the original owners of these photos have an issue with my use of any of the photos used or stored in this repo, let me know and I will remove them immediately. 


## Plans for future updates
* More details on how the face detection technologies work, including details on the hyperparameters
* ~~Add additional face detection technology examples~~ Complete
* Show how MTCNN alters the color schemes of the photos "pre whitened tensors" and how you can change them back 
* Benchmarking scripts to quickly test the speed of each face detection option on a particular piece of hardware, as well as accuracy 
* Implement the face detectors in real time using video  
* Brief example of how the face detectors can be used as a front-end for facial recognition 


### References
* The original data files for Haar Cascade can be found [here](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_fullbody.xml)
* This repo was both inspired and informed by:
    * [Tim Esler's Facenet-PyTorch](https://github.com/timesler/facenet-pytorch)
    * [The pyimagesearch web site created by Adrian Rosebrock, Phd](https://pyimagesearch.com/start-here/)

Thanks to both of you for making what seemed at first a daunting subject, straight forward and easy to learn. 
