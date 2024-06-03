import time
import fontstyle
import paras
import timer 
text = fontstyle.apply('\t\t\t Typing speed '.upper(),'bold/italic/underline/light blue_bg')
text1 = fontstyle.apply('\t\t Test your Typing Speed here!!!','italic')
print(text)
print(text1)

def choose(n):
    if n == 1:
        text2 = fontstyle.apply('Lets Start! Type the Following','bold/italic/green')
        print(text2)
        print()
        p1=paras.paragraphs()
        print(p1)
        print()
        t1=time.time()
        txt_in = input('START TYPING: ')
        t2 = time.time()
        print(timer.mistake(p1,txt_in))
        print(timer.time_taken(t1,t2,txt_in))
        t3 = fontstyle.apply('Thankyou! play again'.upper(), 'bold/italic/white/red_bg')
        print(t3)
    elif n==2:
        stmt = fontstyle.apply('ThankYou!', 'bold/italic/white/red_bg')
        print(stmt)
    else:
        t4= fontstyle.apply('Please enter a valid number','bold/italic/red')      
        print(t4)

