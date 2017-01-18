## Adult

### Characteristics

Train dataset
<table>
    <tr> <td>Number of observations</td> <td>32561</td> </tr>
    <tr> <td>Number of features</td> <td>123</td> </tr>
    <tr> <td>Sparsity</td> <td>11.3%</td> </tr>
    <tr> <td>Class balancing</td> <td>24.1% positive samples</td> </tr>
</table>

Test dataset
<table>
    <tr> <td>Number of observations</td> <td>16281</td> </tr>
    <tr> <td>Number of features</td> <td>123</td> </tr>
    <tr> <td>Sparsity</td> <td>11.4%</td> </tr>
    <tr> <td>Class balancing</td> <td>23.6% positive samples</td> </tr>
</table>

### Description

Predict whether income exceeds $50K/yr based on census data. Also known 
as "Census Income" dataset.
[https://archive.ics.uci.edu/ml/datasets/Adult](https://archive.ics.uci.edu/ml/datasets/Adult)

### Preprocessing
The original Adult data set has 14 features, among which six are continuous and 
eight are categorical. In this data set, continuous features are discretized 
into quintiles, and each quantile is represented by a binary feature. Also, 
a categorical feature with m categories is converted to m binary features. It
leads to a total of 123 binary features. 

John C. Platt. 
Fast training of support vector machines using sequential minimal optimization. 
In Bernhard Schölkopf, Christopher J. C. Burges, and 
Alexander J. Smola, editors, Advances in Kernel Methods - 
Support Vector Learning, Cambridge, MA, 1998. MIT Press.

Note that as feature 122 was not occurring in the test set it has been added 
(with a zero value) to the first observation. Hence train and test data have 
the same number of features. The last line of the original test dataset 
(which only contained a label) has also been removed.

### Original download link
[http://leon.bottou.org/_media/papers/lasvm-adult.tar.bz2](http://leon.bottou.org/_media/papers/lasvm-adult.tar.bz2)