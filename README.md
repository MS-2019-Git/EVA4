# EVA4

#Session1

Answer 1: Channel is a container of a specific related kind of information.Kernel helps to extract this information.
A kernel is a 3X3 feature extractor.Each filter will have one channel of its own.

Answer 2: Using 3X3,we can have any kernel.The odd number 3 is chosen to maintain the symmetry. Every single 3X3 is a superset of any 2X2.

Answer 3: 
199X199> 197X197> 195X195> 193X193> 191X191> 189X189> 187X187> 185X185> 183X183> 181X181> 179X179> 177X177> 175X175> 173X173> 171X171> 169X169> 167X167> 165X165> 163X163> 161X161> 159X159> 157X157> 155X155> 153X153> 151X151> 149X149> 147X147> 145X145> 143X143> 141X141> 139X139> 137X137> 135X135> 133X133> 131X131> 129X129> 127X127> 125X125> 123X123> 121X121> 119X119> 117X117> 115X115> 113X113> 111X111> 109X109> 107X107> 105X105> 103X103> 101X101> 99X99> 97X97> 95X95> 93X93> 91X91> 89X89> 87X87> 85X85> 83X83> 81X81> 79X79> 77X77> 75X75> 73X73> 71X71> 69X69> 67X67> 65X65> 63X63> 61X61> 59X59> 57X57> 55X55> 53X53> 51X51> 49X49> 47X47> 45X45> 43X43> 41X41> 39X39> 37X37> 35X35> 33X33> 31X31> 29X29> 27X27> 25X25> 23X23> 21X21> 19X19> 17X17> 15X15> 13X13> 11X11> 9X9> 7X7> 5X5> 3X3> 1X1


ANSWER 4 :  Kernels are randonly initialized . Finding these random values is called model training.

ANSWER 5: During the training of a DNN, 4 blocks of operations happens . Edges&gradients are converted into textures&patterns , which are then converted into parts of objects and finally converted to objects. This replicates the functioning of the 4 layers of the brain.

#Session2
Test set: Average loss: 1.8768, Accuracy: 2880/10000 (29%)
# Relu activation at the sacrosanct layer is not required 
#x = F.relu(self.conv7(x))
		
Test set: Average loss: 0.0653, Accuracy: 9793/10000 (98%)