## Bund Future trade data

### Description

One month of data in April 2014 on Bund Future traded at eurex with 
microsecond timestamp resolution.

This data is meant to be fitted with Hawkes processes. It contains for each 
day 4 time series representing:

1. Mid-price movement up
2. Mid-price movement down
3. Buyer initiated trades that do not move the mid-price
4. Seller initiated trades that do not move the mid-price

### Characteristics

<table>
    <tr> <td>Number of realizations</td> <td>20</td> </tr>
    <tr> <td>Average number of ticks node 0</td> <td>7009.15</td> </tr>
    <tr> <td>Average number of ticks node 1</td> <td>6998.15</td> </tr>
    <tr> <td>Average number of ticks node 2</td> <td>257677.55</td> </tr>
    <tr> <td>Average number of ticks node 3</td> <td>261423.6</td> </tr>
</table>

### Preprocessing

Market opens at 8AM which corresponds to a timestamp of 28800. This timestamp
has been substracted to all timestamps to have a realizations that starts at 
time 0.

Please note that as markets closes at 10PM, the end time of our 
substracted realizations is 50400. 

