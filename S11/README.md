SuperConvergence
--------------------

Assignment:

Write a code that draws this curve (without the arrows). In submission, you'll upload your drawn curve and code for that
11s11.png

Write a code which uses this new ResNet Architecture for Cifar10:

PrepLayer - Conv 3x3 s1, p1) >> BN >> RELU [64k]

Layer1 -

X = Conv 3x3 (s1, p1) >> MaxPool2D >> BN >> RELU [128k]

R1 = ResBlock( (Conv-BN-ReLU-Conv-BN-ReLU))(X) [128k] 

Add(X, R1)

Layer 2 -

Conv 3x3 [256k]

MaxPooling2D

BN

ReLU

Layer 3 -
X = Conv 3x3 (s1, p1) >> MaxPool2D >> BN >> RELU [512k]

R2 = ResBlock( (Conv-BN-ReLU-Conv-BN-ReLU))(X) [512k]

Add(X, R2)

MaxPooling with Kernel Size 4

FC Layer 

SoftMax

Uses One Cycle Policy such that:
Total Epochs = 24
Max at Epoch = 5
LRMIN = FIND
LRMAX = FIND
NO Annihilation

Uses this transform -RandomCrop 32, 32 (after padding of 4) >> FlipLR >> Followed by CutOut(8, 8)
Batch size = 512
Target Accuracy: 90%.

The lesser the modular your code is (i.e. more the code you have written in your Colab file), less marks you'd get. 
Questions asked are:
Upload the code you used to draw your ZIGZAG or CYCLIC TRIANGLE plot.
Upload your triangle Plot which was drawn with your code.
Upload the link to your GitHub copy of Colab Code. 
Upload the github link for the model as described in A11. 
What is your test accuracy?

