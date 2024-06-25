if 'email to harry' in jarvis:
    try:
        sperak=("what should I say")
        content = takecommand()
        to="mohiteakshy2002@gmail.com"
        sendEmail(to,content)
        speak("email has been sent!")
    except  Exception as e:
        print (e)
        speak("sorry my friend harry bhai ,i am not able to send this email")
else:
  print("no query matched")           
    
        