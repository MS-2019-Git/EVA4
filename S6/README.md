Session6 Problem Statement:In this session , the goal is to understand how L1 & L2 weight decay works with respect to batchsize. What is the impact on the DNN model when we use very large or very small value of L1 and L2. 

For 40 epochs,
without L1/L2
with L1
with L2
with L1 and L2


Validation Accuracy and Loss change Graph Path:
-------------------------------------------------



RESULTS FROM 4CASES ARE:
-------------------------

CASE1: NO L1/L2 	Acc=99.19%  Val_ac=99.47% at 40th Epoch
CASE2: L1 Applied 	Acc=99.23%  Val_ac=99.47% at 40th Epoch
CASE3: L2 Applied 	Acc=98.52%  Val_ac=98.96% at 40th Epoch
CASE4: L1&L2 Applied 	Acc=98.60%  Val_ac=98.78% at 40th Epoch


Analysis of the model with different scenarios of L1 and L2 application:
-----------------------------------------------------------------------

1) At the first case where no L1 or L2 is applied, the target val_acc is in the range of 99.35 to 99.40 but there is a clear case of underfitting.

2)On applying L1 regularization of factor=0.00025 to the loss, the underfitting is reduced to some extent but is still there.Also, the val_acc is below the 99.35 across epochs.

3) The underfitting vanishes to large extent upon L2 regularization of weight decay=0.005. But the acc and val_acc itself values reduced also.

4) When we tried both weight decay and L1 , traces of underfitting is still there but very less but the accuracies are lesser than the target of 99.4 still.



