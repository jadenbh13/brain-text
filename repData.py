import datetime
import random
import serial
import time
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from twilio.rest import Client
from pynput.keyboard import Key, Controller
keyboard = Controller()
# Your Account SID from twilio.com/console
account_sid = "ACCNT_SID"
# Your Auth Token from twilio.com/console
auth_token  = "ACCNT_TOKEN"
# /dev/tty.SLAB_USBtoUART
# /dev/tty.usbmodem1411

client = Client(account_sid, auth_token)
toStr = 'RECIPIENT_PHONE_NUMBER'
COM = '/dev/tty.SLAB_USBtoUART'# /dev/tty.SLAB_USBtoUART
BAUD = 9600

ser = serial.Serial(COM, BAUD, timeout = .1)

print('Waiting for device');
time.sleep(3)
print(ser.name)

char = 0
charList = [0]

def read_data():
    global char
    global charList
    m = 0
    n = 0
    #Get serial output from nodemcu
    val = str(ser.readline().decode().strip('\r\n'))
    print(val)
    e = val.split(',')
    #If brain data is sent
    if len(e) > 4:
        #Get high and low alpha waves
        l = int(e[6]) + int(e[7])
        #Average them for single alpha wave value
        num = l / 2
        nuu = int(e[7])
        print(num)
        #If alpha waves are greater than 9000(user is focusing)
        if num > 9000:
            #Append current char to charList
            charList.append(char)
            print("Added")
        #If not
        else:
            #Add 1 to char
            char += 1
            #If char is greater than 9
            if char > 9:
                #Reset to 0(start from top)
                char = 0
        """if len(charList) % 3 == 0:
            charList.append(0)"""
        print("    ")
        print(char)
        print(charList)
        print("    ")
        m = num
        n = nuu
    #Return alpha wave values
    return m, n


def animate(frame, xs, ys):


    # Read data
    dat = read_data()
    #Correspond x axis with seconds elapsed
    xs.append(datetime.datetime.now().strftime('%S'))
    #Correspond y axis with alpha wave values
    ys.append(dat[0])
    #Set limits for graph
    size_limit = 30
    xs = xs[-size_limit:]
    ys = ys[-size_limit:]
    #Clear axes and plot x and y
    ax.clear()
    ax.plot(xs, ys)
    #Set values for plot
    plt.grid()
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)

    plt.title('Brain wave data')
    plt.ylabel('Alpha wave amplitude')
    plt.xlabel('Time')


if __name__ == '__main__':
    e = 0
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    x_data = []
    y_data = []
    #Show plot
    ani = animation.FuncAnimation(fig, animate, fargs=(x_data, y_data), interval=200)
    plt.show()
    #Once exited
    print("    ")
    h = 0
    lst = []
    mnLst = []
    sts = ""
    #Loop through charList
    while h < len(charList):
        print("   ")
        print(h)
        print(charList[h])
        #Append current index to lst
        lst.append(charList[h])
        print(lst)
        #For every 2 values:
        if h % 2 == 0:
            if len(lst) == 3:
                vb = [lst[1], lst[2]]
                mnLst.append(vb)
            #Append lst to mnLst
            mnLst.append(lst)
            #Reset lst(keep to 2 values)
            lst = []
        print("   ")
        h += 1
    print(charList)
    #Loop through mnLst
    for b in mnLst:
        #If length of current index is greater than 1(there exists a 2 number ASCII code at current index)
        if len(b) > 1:
            #Create empty string
            st = ""
            #Loop through each number
            for j in b:
                #Add string of j to string(creates a string of numbers)
                st += str(j)
            #Convert st to integer
            chars = int(st)
            print(chars)
            #Convert from ASCII code to actual letter
            print(chr(chars))
            #Add letter to string of all letters
            sts += chr(chars)
    print(mnLst)
    print(sts)
    print(toStr)
    #Call to twilio messages(create sms message)
    #Use string of ASCII letters to fill body
    #Use previously defined recipient string to fill to value
    message = client.messages \
                    .create(
                         body=sts,
                         from_='TWILIO_PHONE_NUMBER',
                         to=toStr
                     )
    #Print message SID to confirm sending
    print(message.sid)
    print("    ")



