
import numpy as np
import sys
from scipy.stats import poisson

# if the user includes the flag -h or --help print the options
if '-h' in sys.argv or '--help' in sys.argv:
    print ("Usage: %s [-seed number]" % sys.argv[0])
    print
    sys.exit(1)

# read the user-provided seed from the command line (if there)
if '-seed' in sys.argv:
    p = sys.argv.index('-seed')
    seed = sys.argv[p+1]
else:
    seed = 2222

if '-size' in sys.argv:
    p = sys.argv.index('-size')
    size = sys.argv[p+1]
else:
    size= 123

# Set the null hypothesis rate of sunny days
Null_rate = 122

# Generate an array of data under the null hypothesis using Poisson distribution
np.random.seed(seed)

sampleN = np.random.poisson(Null_rate, size)
with open("poisson_arr.txt", "w") as fileN:
    np.savetxt(fileN, sampleN)

# Generate probability mass function(PMF) for Poisson distribution with the null hypothesis rate
A = np.arange(50, 200)
B = poisson.pmf(A, Null_rate)
with open("poisson_pmf.txt", "w") as filex:
    np.savetxt(filex, B)




