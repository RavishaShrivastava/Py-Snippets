#importing user-defined module
import paras

#for displaying time taken by the user
def time_taken(t1,t2,type1):

    #t1= time taken in the starting
    #t2= time taken after typing
    time_taken = t2 - t1
    
    #rounding of the time taken to 2 decimal places
    round_time_taken = round(time_taken, 2) #displayed in seconds

    #speed display word per seconds
    speed = round((len(type1) // round_time_taken),0)

    #displaying the output
    return f'Time Taken: {round_time_taken}seconds\nSpeed: {speed}w/s'

#definig to count the error done by user
def mistake(n,m):
    #n= text displayed by program 
    #m= text written by user
    
    error = 0 #initialing error as 0
    
    #matching each letter of the displayed text and text written by user
    for i in range(len(n)):
        try:
           #if both the text are not equal then error is increased by 1
            if n[i] != m[i]:
                error += 1
        except:
            # may rise IndexError if sentence written by user is incomplete 
            error+=1

    #conclusion
    return f'\nERROR: {error}'
