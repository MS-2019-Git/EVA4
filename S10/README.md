1) Main Solution File:
  https://github.com/MohuaSinha/EVA4/blob/master/S10/S10_Solution_Main.ipynb
  
2)  Images_GradCam folder contains .png files after running GradCam on any 25 misclassified images.The prediction and ground truth label is marked.
  
  
3) CutOut is added from tranformations[Albumentations].
4) LR finder implemented for SGD with momentum
5) ReduceLROnPlateau implemented.
6) Epochs=50 , Model Used=ResNet18
7) Accuracy_change.png is the graph for training and test accuracy change.

Library contains below 11 modules in python files:
--------------------------------------------------

config.py
datatransformation.py
displayimages.py
dnnmodel.py
gradcam.py
grad_visualize.py
lr_finder.py
plotresults.py
showimages.py
train_test.py
utils.py
