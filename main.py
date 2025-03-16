import scratchattach
import webview

sessions=[]

class JSAPIObject:
    def __init__(self):
        pass
    def login(self,username,password):
        print(username,password)
        try:
            session=scratchattach.login(username,password)
        except:
            return False
        else:
            sessions.append(session)
            return True

js_api=JSAPIObject()

window=webview.create_window("Scratch for desktop",html=open("main.html").read(),js_api=js_api)
webview.start()