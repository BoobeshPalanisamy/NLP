# ChatBot for Hotel Management(All through voice to text classifications)

import speech_recognition as sr 
import pyttsx3
from nltk.tokenize import word_tokenize

def text_to_speech(txt):
    text_speech = pyttsx3.init()
    text = txt
    print(txt)
    text_speech.say(text)
    text_speech.runAndWait()  
        
def speech_to_text(txt):
    r = sr.Recognizer()    
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            txt.append(text)
            print(txt)
        except:
            print('sorry could not recognize your voice')
            speech_to_text(txt)                            

customer_details = {}
 
def reg_name():
    text_to_speech('To Book room we want some details, can I know your good name please')
    b=[]
    speech_to_text(b)
    customer_details['name']=b[0]
    if len(b)>0:
        reg_mob()
    else:
        reg_name()        
    
def reg_mob():
    text_to_speech('Please enter your Mobile Number')
    c=[]
    speech_to_text(c)
    customer_details['contact No.']=c[0]
    if len(c)>0:
        reg_add()
    else:
        reg_mob()        

def reg_add():
    text_to_speech('Please enter you address')
    d=[]
    speech_to_text(d)
    customer_details['address']=d[0]
    if len(d)>0:
        reg_ID()
    else:
        reg_add() 
    
def reg_ID():
    text_to_speech('Please mention any ID proof you have')
    e=[]
    speech_to_text(e)
    customer_details['ID Proof']=e[0]
    if len(e)>0:
        reg_ID_No()
    else:
        reg_ID() 
    
def reg_ID_No():
    text_to_speech('Please enter ID number of proof you mentioned')
    f=[]
    speech_to_text(f)
    customer_details['ID Proof No.']=f[0]
    if len(f)>0:
        reg_room_type()
    else:
        reg_ID_No() 
    
def reg_room_type():
    text_to_speech('Which type of room do you want, In our hotel ac, nonac, suit rooms are available')
    g=[]
    speech_to_text(g)
    customer_details['room type']=g[0]
    if len(g)>0:
        reg_arriv_date()
    else:
        reg_room_type() 
    
def reg_arriv_date():
    text_to_speech('Please enter date of check IN')
    h=[]
    speech_to_text(h)
    customer_details['arrival date']=h[0]
    if len(h)>0:
        reg_dep_date()
    else:
        reg_arriv_date() 
    
def reg_dep_date():
    text_to_speech('Please enter date of check out')
    i=[]
    speech_to_text(i)
    customer_details['departure date']=i[0]
    if len(i)>0:
        text_to_speech('Your booking is registered')
        text_to_speech('for payment and further details you can contact our help desk any time')
        text_to_speech('thank you have a nice day')
    else:
        reg_dep_date() 
  
text_to_speech('Welcome to HotelParadise, This is ChatBot, How can I help you?')   

a=[]
speech_to_text(a)
if 'book' in a[0] and 'room' in a[0]:
    reg_name()
else:
    text_to_speech('sorry I cant understand,for any other services you contact our helpdesk')
    text_to_speech('thank you have a nice day')
            
        
print(customer_details)      
         
file = open('Hotel_Customer_details.txt','a')
file.write(str(customer_details))
file.write(" ")
file.write("\n")
file.close()
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         