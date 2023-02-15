
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t
import math as mt

# Load the Poisson distribution and Poisson PMF from the text file
with open("poisson_arr.txt", "r") as fileN:
    sampleN= np.loadtxt(fileN)
with open("poisson_pmf.txt", "r") as filex:
    y1 = np.loadtxt(filex)

# The null hypothesis rate of sunny days
null_rate = 122

# Plot the histogram of the sample data for null hypothesis 
plt.hist(sampleN, bins=range(0, 200, 6), density=True, alpha=0.7, label="Sample data", color='skyblue', edgecolor='black')

# Plot the Poisson PMF with the null hypothesis
A = np.arange(50, 200)
plt.plot(A, y1, '--', linewidth=2,label="Poisson PMF\nwith Sunny days rate = 122")

# Calculate the sample data standard deviation and sample mean 
data_std = np.std(sampleN)
data_mean = np.mean(sampleN)


# Plot a vertical line for the sample mean
plt.axvline(data_mean, color='red', linewidth=1.5, label="The mean of data")

# Calculate the confidence interval of 90%
interval1 = np.percentile(sampleN, 90)
print('interval 90%=', interval1)

#Plot a vertical line for the confidence interval of 90%
plt.axvline(interval1, color='Pink', linestyle='dashed', linewidth=1.5, label='Significance Level 90%')


# Calculate the confidence interval of 95%
interval2 = np.percentile(sampleN, 95)
print('interval 95%=', interval2)


#Plot a vertical line for the confidence interval of 95%
plt.axvline(interval2, color='green', linestyle='dashed', linewidth=1.5, label='Significance Level 95%')

# Calculate the test statistic and p-value
dof = np.size(sampleN) - 1
stand_err=(data_std / mt.sqrt(np.size(sampleN)))
t_statist = (data_mean - null_rate) / stand_err
p_val = 1 - t.cdf(t_statist, dof)
print('pvalue=', p_val)

# Add a title, labels legends, and save the plot
plt.title("Poisson distribution and Student's t-test")
plt.xlabel("Number of sunny days")
plt.ylabel("Probability")
plt.legend()
plt.savefig('Piosson.png')

# Show the plot
exec('plt.show()')

# Set alpha=0.05 and make a dision for the null hypothesis
if p_val < 0.1 or p_val==0.1:
    print('Reject the null hypothesis with alpha 10%')
else:
    print("Fail to reject the null hypothesis with alpha 10%.")
        

# Set alpha=0.05 and make a dision for the null hypothesis
if p_val < 0.05 or p_val==0.05:
    print('Reject the null hypothesis with alpha 5% ')
else:
    print("Fail to reject the null hypothesis with alpha 5% ")
        
