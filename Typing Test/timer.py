import paras
def time_taken(t1,t2,type1):
    time_taken = t2 - t1
    round_time_taken = round(time_taken, 2)
    speed = round((len(type1) // round_time_taken),0)
    return f'Time Taken: {round_time_taken}seconds\nSpeed: {speed}w/s'

def mistake(n,m):
    error = 0
    for i in range(len(n)):
        try:
            if n[i] != m[i]:
                error += 1
        except:
            error+=1
    return f'\nERROR: {error}'
