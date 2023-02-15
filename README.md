# Hypothesis Test for the rate of Sunny Days per Year
The code in this repository is written to simulate a categorical distribution of weather condition and test if we will have more sunny days rate for the next year or not using Poisson distribution and student t-test.
# How to run the code?
1. Run `WeatherCategory.py` this will write and read text file name 'expected w.txt' and then will plot and save a bar diagram `plot1.png` that shows the counts of day according to category function from 'Random.py' file. you can type: `python3 WeatherCategory.py -seed <seed_number> -Nday <number of days>`  .
I set the default to be seed=7777 and Nday=356


2. Run `poisson_data.py'. this will write to two text files with names `poisson_arr.txt` and `poisson_pmf.txt`. In case you want to change the sample size, you will need to change from inside the python file. I set the default seed= 2222, size=123 Null_rate=122

3. Run `poisson_analysis.py`. This will plot and save `poisson.png` that show poisson pmf and the confidence interval of 90% and 95%. Also will print p-value and make decision about the null hypothesis. 


