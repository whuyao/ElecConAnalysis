**Open source library**

pymongo-3.11.0 ，matplotlib-3.1.3	，

numpy-1.18.1，pandas-1.0.1，

scikit-learn-0.22.1，pyarc-1.0.25，

GDAL-3.1.2



**Gets_the_location_where_power_consumption_occurs**

Match the power consumption data and site location based on the site number.



**Update_geographic_coordinates**
According to the address matching results of Gao DE map and Baidu Map, the number of distribution stations lacking geographical coordinates is reduced.



**Geocoding_for_csv**

The latitude and longitude coordinates of the distribution station are obtained through baidu map API according to the fuzzy place names of the distribution station, and the information of the power station with abnormal matching is given.



**Normalization of training set data**

Batch normalized data of each driver in the training set and record the parameters in the normalization process.



**Regression_model_selection**

By comparing the performance of different regression algorithms with the same set of data, the model most suitable for the experimental data was selected.



**Get the best parameters**

By controlling the variables, the optimal decision tree tree and the maximum characteristic number of the random forest model in the experimental scene were determined.



**Establish the power consumption model**

基于随机森林算法，预训练得到电力消耗分布模型，并且返回训练的模型精度，影响因子的重要性排行等信息。



**Mapping of power consumption distribution**

Based on the random forest algorithm, the power consumption distribution model is obtained through pre-training, and information such as the model accuracy of training and the importance ranking of impact factors is returned.



**Chart the importance of drivers**

According to the importance of driving factors in the model training process, draw the importance ranking of different regions



**Plot the relationship between electricity consumption and GDP**

Explore the correlation between power consumption and gross regional product, and draw an image

















