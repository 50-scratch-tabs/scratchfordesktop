import scratchattach
import webview

window=webview.create_window("Scratch for desktop",html=open("main.html").read())
webview.start()