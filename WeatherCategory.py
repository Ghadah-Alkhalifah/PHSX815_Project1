from Random import Random
import numpy as np
import matplotlib.pyplot as plt
import sys


# main function for our coin toss Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print
        sys.exit(1)

    #defualt seed 
    seed=7777
    # Number of observed days (expermints) 
    Nday=365
    
    

    # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]
    if '-Nday' in sys.argv:
        p = sys.argv.index('-Nday')
        Nt1 = int(sys.argv[p+1])
        if Nt1 > 0:
            Nday = Nt1
    

    # class instance of our Random class using seed
    randomNum = Random(seed)
    y0 =[]
    
    for i in range(0,Nday):
        y0.append(randomNum.Weather0())
        
    
    
    
    # write text file for categorical probability
    fileW=open('expected w.txt', "w")
    C=str(y0)
    fileW.write(C)
    fileW.close()

    # read the text file for the categorical probability
    fileR = open('expected w.txt', 'r')
    Lines = fileR.readlines()
    
    # counting the accurance of weather condition
    counting_s=[]
    counting_r=[]
    counting_c=[]
    count_accu= []
    
    for line in Lines:
        counting2=line.count('2')
        counting_s.append(counting2)
    
    totals=np.sum(counting_s)
    count_accu.append(totals)
    for line in Lines:
        counting1=line.count('1')
        counting_r.append(counting1)

    totalr=np.sum(counting_r)
    count_accu.append(totalr)
    for line in Lines:
        counting0=line.count('0')
        counting_c.append(counting0)
    
    totalc=np.sum(counting_c)
    count_accu.append(totalc)
    
    

    #ploting bar graph showing accurance of weather condition 
    category= [ 'Sunny' , 'Rainy', 'Cloudy']
    plt.bar(category, count_accu, width=.4, bottom=None, color='g')
    plt.title('Weather condition vs frequent accurance')
    plt.xlabel('Weather condition')
    plt.ylabel('accurance (days)')
    plt.grid()
    plt.savefig('plot1.png')
    plt.show()
    
    
    






    

            
        

    
        





    
