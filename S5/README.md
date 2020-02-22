
Session 5 : Final Code7 is able to get 99.4 test accuracy with 15 epochs and 9.4K parameters.




MY CODE1: BASIC STRUCTURE WITH 10 Output_channels
-------------------------------------------------

This is what i have started with the [S5:Code3(Lighter model)]. 
The REASON why i started with this:
 1) This is the basic code with convolution2d,maxpooling,relu and output channels starting with 10. 
 2) This gives a better lower number of parameters as compared to the [S5:Code2(Basic Skeleton)] 
	 which uses output channels from 32 leading to more number of parameters and a glimpse of overfitting as well.
	 
Target: 1. Get a good model with basic stuffs like transforms,data loader,basic working code,lighter model with lower no. of parameters.
		2. No over-fitting possibly.
		
Results: Parameters= 10,790
		 Best Train Accuracy 98.92
		 Best Test Accuracy  98.86
		 
Analysis: 		 
       1. No Over fitting and model is lighter with low no. of parameters
	   2. But the expected accuracy is way lesser.
	   
	   
	   
MY CODE2: BATCHNORM
--------------------

Target: 1. Adding BatchNormalization to increase model efficiency/accuracy.
		2. No over-fitting possibly.
		
Results: Parameters= 10,790
		 Best Train Accuracy 99.90
		 Best Test Accuracy  99.27
		 
Analysis: 		 
       1. Over fitting introduced again.
	   2. Still the test accuracy is way lesser than the target of 99.4
	   
	   
MY CODE3: GAP
----------------

Target: 1. Ideally Overfitting should be handled with regularization but here i want to check the effect of GAP(Global average pooling) on this existing model.
		
		
Results: Parameters= 6,070
		 Best Train Accuracy 99.08
		 Best Test Accuracy  98.93
		 
Analysis: 		 
       1. GAP reduces the number of parameters 40% almost.
	   2. The test accuracy reduced but no over-fitting.
       3. Next model i will try to increase the accuracy


MY CODE4: INCREASING CAPACITY/LAYERS
------------------------------------

Target: 1. To add more convolution layers 
		
Results: Parameters= 9,434
		 Best Train Accuracy 99.50(12th Epoch)
		 Best Test Accuracy  99.34 (12th Epoch)
		 
Analysis: 		 
       1. Additional layer helped to increase the accuracy and able to see 99.34 at 12th Epoch but subsequent epochs are not CONSISTENT.
	   2. NO Over fitting
       3. Number of Parameters increased(within 10K target) but accuracy also increaed.	  

MY CODE5: IMAGE AUGMENTATION
-----------------------------

Target: 1.Adding Image rotation of 7 degrees 
		
Results: Parameters= 9,434
		 Best Train Accuracy 99.40(17th Epoch)
		 Best Test Accuracy  99.36(17th Epoch)
		 
Analysis: 
		1. Image Rotation has almost same impact but accuracy is stable for subsequent epochs
		2. Still my accuracy is not at target. next model will add regularization.
		
MY CODE6: REGULARIZATION
------------------------
		
Target: 1.Adding Dropout 
		
Results: Parameters= 9,434
		 Best Train Accuracy 98.96
		 Best Test Accuracy  99.03
		 
Analysis:		
		1. UNDER-FITTING is evident.
		2. I will try LR Scheduler in next model .
		
		
MY CODE7: LR Scheduler and ADDing more layers after GAP
------------------------------------------------
		
Target: 1.Working on LR scheduler
		
Results: LR Scheduler:
		 Parameters= 9,434
		 Best Train Accuracy 99.01
		 Best Test Accuracy  99.14
		 
		 With Additional Conv layers
		 Parameters=9,810
		 Best Train Accuracy 98.93
		 Best Test Accuracy  99.40
		 
Analysis:		
		1. LR scheduler made the acuracy stable but to achieve better accuracy in lesser number of epochs,added conv layers 
		
         		
	   
	   
	   
	   
	   