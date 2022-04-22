# Face Detection Examples -- WORK IN PROGRESS 

Basic tutorials/examples depicting the performance, accuracy and other characteristics of a couple of face detection technologies. 

Note:
* To avoid running afoul of Github's limits on large files, I didn't upload the underlying model files for Haar Cascade, 


## Plans for future updates
* More details on how the face detection technologies work, including details on the hyperparameters
* Add additional face detection technology examples 
* Show how MTCNN alters the color schemes of the photos "pre whitened tensors" and how you can change them back 
* Benchmarking scripts to quickly test the speed of each face detection option on a particular piece of hardware, as well as accuracy 
* Implement the face detectors in real time using video  
* Brief example of how the face detectors can be used as a front-end for facial recognition 


### Update History
* **4/21/2022:** initial commit with examples of facial detection using Haar Cascade with OpenCV and MTCNN, including external helper scripts for the Jupyter Notebook, and sample image files  

### References
* The original data files for Haar Cascade can be found [here](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_fullbody.xml)
* This repo was both inspired and informed by:
    * [Tim Esler's Facenet-PyTorch](https://github.com/timesler/facenet-pytorch)
    * [The pyimagesearch web site created by Adrian Rosebrock, Phd](https://pyimagesearch.com/start-here/)

Thanks to both of you for making what seemed at first a daunting subject, straight forward and easy to learn. 