import webbrowser
import pyttsx3

engine = pyttsx3.init()
user = input('User : ')

if user=='Hi chatbot':
    print('Hi')
    engine.say ( 'Hi' )
    engine.runAndWait ( )
    print ('I am chatbot...')
    engine.say ( 'I am chatbot' )
    engine.runAndWait ( )
    print('May I know your name???')
    engine.say ( 'May I know your name???' )
    engine.runAndWait ( )
    word1 = input('User : ')
    print('')
    print('Hi '+word1)
    engine.say('Hi'+word1)
    engine.runAndWait ( )
    print ( 'How are you??')
    engine.say('How are you')
    engine.runAndWait ( )
    word2 = input('User : ')
    if word2=='I am fine':
        print('')
        print('Glad to hear that')
        engine.say ( 'Glad to hear that' )
        engine.runAndWait()
        print('I am also fine')
        engine.say ( 'I am also fine' )
        engine.runAndWait()
        print('')
        print('How may I help you ???')
        engine.say('How may I help you')
        engine.runAndWait()
        work1 = input('User : ')
        #Brower works.....
        if work1=='google':
            webbrowser.open_new_tab('www.google.com')
        elif work1=='youtube':
            webbrowser.open_new_tab('www.youtube.com')
        elif work1=='amazon':
            webbrowser.open_new_tab('www.amazon.in')
        elif work1=='instagram':
            webbrowser.open_new_tab('www.instagram.com')
        elif work1=='github':
            webbrowser.open_new_tab('www.github.com'
        else:
            print('Invalid input !!!!!!!!')
            engine.say ( 'Invalid input !!!!!!!!' )
            engine.runAndWait ( )
            print('Working functions are given below :---')
            engine.say ('Working functions are given below')
            engine.runAndWait ( )
            print ('1) Open google')
            print ('2) Open youtube')
            print ('3) Open amazon')
    else:
        print('Invalid Input !!!!')
else:
    print('Invalid Input!!!!')
    print('Type the first letter in uppercase only')
