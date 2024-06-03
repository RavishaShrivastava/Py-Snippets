#importing modules
import time #To track the time
import fontstyle #Used for styling of the fonts 
import paras #user-predefined
import timer #user-predefined

#Displaying welcoming message 
text = fontstyle.apply('\t\t\t Typing speed '.upper(),'bold/italic/underline/light blue_bg')
text1 = fontstyle.apply('\t\t Test your Typing Speed here!!!','italic')
print(text)
print(text1)

def choose(n):
    if n == 1: 
    #When Start is chosen if block will be executed
        
        text2 = fontstyle.apply('Lets Start! Type the Following','bold/italic/green')
        #starting the game
        print(text2)
        print()

        p1=paras.paragraphs()
        #Random line selected from paras(user-defined) module 
        print(p1)
        print()
        
        t1=time.time() #time noted in the start
        txt_in = input('START TYPING: ')
        t2 = time.time() #time noted in the end

        #importing mistake to count error done by user from timer
        print(timer.mistake(p1,txt_in))

        #importing time_taken to know the time taken by user 
        print(timer.time_taken(t1,t2,txt_in))

        #displaying conclusion message
        t3 = fontstyle.apply('Thankyou! play again'.upper(), 'bold/italic/white/red_bg')
        print(t3)
        
    elif n==2: 
    #When exit is chosen elif block will be excuted
        stmt = fontstyle.apply('ThankYou!', 'bold/italic/white/red_bg')
        print(stmt)
        
    else:
    #When any other number is chosen else block will be excuted
        t4= fontstyle.apply('Please enter a valid number','bold/italic/red')      
        print(t4)

