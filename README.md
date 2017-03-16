Below are the outputs of my program for value of information gain set to 1.0, 0.1 and 0. Each line of output is described as 
FeatureVal(best feature to split on)	nPosNeg     Gain

The last line indicates the Accuracy of the classifier with particular minimum gain.

Summary of the Accuracies:
Minimum Gain	Accuracy
1.0		0.513863216266
0.1		0.994454713494
0		1.0


######################################################################################################################
python id3.py train test 1
>FeatureVal(feature='Predict ', value='e')      (3122, 2878)    1.0
0.513863216266

#######################################################################################################################
python id3.py train test 0.1
>FeatureVal(feature=5, value='n')       	(3122, 2878)    0.5332179824444057
->FeatureVal(feature=20, value='r')     	(2523, 79)      0.10329266813795125
-->FeatureVal(feature='Predict ', value='p')    (0, 48) 	0.0
-->FeatureVal(feature='Predict ', value='e')    (2523, 31)      0.061541524213776004
->FeatureVal(feature=4, value='f')      	(599, 2799)     0.38557073463169284
-->FeatureVal(feature='Predict ', value='p')    (0, 2397)       0.0
-->FeatureVal(feature=11, value='c')    	(599, 402)      0.3985075001359971
--->FeatureVal(feature='Predict ', value='e')   (385, 0)        0.0
--->FeatureVal(feature=11, value='r')   	(214, 402)      0.4812488002746312
---->FeatureVal(feature='Predict ', value='e')  (147, 0)        0.0
---->FeatureVal(feature=7, value='c')   	(67, 402)       0.5916727785823275
----->FeatureVal(feature='Predict ', value='p') (0, 402)        0.0
----->FeatureVal(feature='Predict ', value='e') (67, 0) 	0.0
0.9944547134935305

#########################################################################################################################
python id3.py train test 0.0
>FeatureVal(feature=5, value='n')       		(3122, 2878)    0.5332179824444057
->FeatureVal(feature=20, value='r')     		(2523, 79)      0.10329266813795125
-->FeatureVal(feature='Predict ', value='p')    	(0, 48) 	0.0
-->FeatureVal(feature=13, value='y')    		(2523, 31)      0.061541524213776004
--->FeatureVal(feature=8, value='b')    		(11, 26)        0.8779620013943912
---->FeatureVal(feature='Predict ', value='e')  	(11, 0) 	0.0
---->FeatureVal(feature='Predict ', value='p')  	(0, 26) 	0.0
--->FeatureVal(feature=2, value='g')    		(2512, 5)       0.011366044026456749
---->FeatureVal(feature='Predict ', value='p')  	(0, 3)  	0.0
---->FeatureVal(feature=1, value='c')   		(2512, 2)       0.004271351235111105
----->FeatureVal(feature='Predict ', value='p') 	(0, 1)  	0.0
----->FeatureVal(feature=8, value='n')  		(2512, 1)       0.001680640203660801
------>FeatureVal(feature=4, value='f') 		(134, 1)        0.0630678080038568
------->FeatureVal(feature='Predict ', value='e')       (134, 0)        0.0
------->FeatureVal(feature='Predict ', value='p')       (0, 1)  	0.0
------>FeatureVal(feature='Predict ', value='e')        (2378, 0)       0.0
->FeatureVal(feature=4, value='t')      		(599, 2799)     0.38557073463169284
-->FeatureVal(feature=11, value='c')    		(599, 402)      0.3985075001359971
--->FeatureVal(feature='Predict ', value='e')   	(385, 0)        0.0
--->FeatureVal(feature=11, value='r')   		(214, 402)      0.4812488002746312
---->FeatureVal(feature='Predict ', value='e')  	(147, 0)        0.0
---->FeatureVal(feature=7, value='c')   		(67, 402)       0.5916727785823275
----->FeatureVal(feature='Predict ', value='p') 	(0, 402)        0.0
----->FeatureVal(feature='Predict ', value='e') 	(67, 0) 	0.0
-->FeatureVal(feature='Predict ', value='p')    	(0, 2397)       0.0
1.0
