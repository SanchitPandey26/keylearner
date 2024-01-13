# importing modules
import tkinter
from tkinter import *
import random
import ttkthemes
from tkinter import ttk
from tkinter import messagebox
from tkinter import Entry
import webbrowser
import time as t



#################FUNCTIONALITY PART
time = 0
wrongwords = 0
elapsed_time_in_minutes = 0
start_time = 0
timeleft = 60
correct_word = 0
wrong_word = 0
i = 0
sliderwords = ''
count_s = 0

def start_timer():
    global time, start_time
    startButton.config(state=DISABLED)
    submitButton.config(state=NORMAL)
    text_area.config(state=NORMAL)
    text_area.focus()
    start_time = t.time()


def count():
    global wrongwords, elapsed_time_in_minutes, start_time, time
    time = round(t.time()-start_time)
    elapsed_timer_label.config(text=time)
    submitButton.config(state=DISABLED)
    text_area.config(state=DISABLED)
    resetButton.config(state=NORMAL)
    entered_paragraph = text_area.get(1.0,END)
    a = entered_paragraph.replace(" ", "")
    totalwords = len(a)
    totalwords_count_label.config(text=totalwords)
    para_word = paragraph_label['text']
    para = para_word.replace(" ","")
    para_word_list = paragraph_label['text'].split()
    size = len(para_word_list)
    length = len(a)
    c = 0
    for x,y in zip(a, para):
        if x == y:
            c += 1
            print(x,y)
        else:
            wrongwords += 1
            print(x,y)
    wrongwords_count_label.config(text=wrongwords)

    elapsed_time_in_minutes = time/60
    wpm = length
    wpm_count_label.config(text=wpm)

    gross_wpm = totalwords/elapsed_time_in_minutes
    accuracy = round((c/wpm)*100)
    accuracy_count_label.config(text=str(accuracy)+'%')


def reset():
    global time, elapsed_time_in_minutes
    time = 0
    elapsed_time_in_minutes = 0
    startButton.config(state=NORMAL)
    resetButton.config(state=DISABLED)
    text_area.config(state=NORMAL)
    text_area.delete(1.0, END)
    text_area.config(state=DISABLED)

    elapsed_timer_label.config(text=0)
    wpm_count_label.config(text=0)
    accuracy_count_label.config(text=0)
    totalwords_count_label.config(text=0)
    wrongwords_count_label.config(text=0)
    random.shuffle(paragraph_list)
    paragraph_label.configure(text=paragraph_list[0])


def speed_test(windows):



    word_list = ['keyboard', 'Eagle', 'Mouse', 'honour', 'giraffe', 'karma', 'Dictionary', 'helium', 'brown', 'Goalkeeper',
                 'house',
                 'Mountain', 'neutral', 'Waffle', 'Monopoly', 'business', 'table', 'Blanket', 'laptop', 'plunger',
                 'Chamber', 'Secrets',
                 'lioness', 'Climber', 'appealing', 'muscles', 'Memory', 'naughty', 'notorious', 'Clumsy', 'harvard',
                 'Alphabet']

    # Functionality part

    def timer():
        global timeleft, i
        if timeleft > 0:
            timeleft -= 1
            time_countLabel.config(text=timeleft)
            time_countLabel.after(1000, timer)
        else:
            wordEntry.config(state=DISABLED)
            result = correct_word - wrong_word
            instructionLabel.config(
                text=f'Correct words {correct_word}\n Wrong Words {wrong_word}\n Final Score {result}')
            if result < 15:
                emoji1Label.config(image=poorpic)
                emoji2Label.config(image=poorpic)
            elif 15 <= result < 30:
                emoji1Label.config(image=goodpic)
                emoji2Label.config(image=goodpic)
            else:
                emoji1Label.config(image=propic)
                emoji2Label.config(image=propic)
            res = messagebox.askyesno('Confirm', 'Do you want to play again?')
            if res:
                i = 0
                timeleft = 60
                countLabel.config(text='0')
                time_countLabel.config(text='60')
                wordEntry.config(state=NORMAL)
                instructionLabel.config(text='Type word and hit Enter')
                emoji1Label.config(image='')
                emoji2Label.config(image='')


    def play_game(event):
        if wordEntry.get() != '':
            global i, correct_word, wrong_word
            i += 1
            countLabel.config(text=i)

            instructionLabel.config(text='')
            if timeleft == 60:
                timer()
            if wordEntry.get() == word_list_Label['text']:
                correct_word += 1
            else:
                wrong_word += 1

            random.shuffle(word_list)
            word_list_Label.config(text=word_list[0])
            wordEntry.delete(0, END)

    def slider():
        global sliderwords, count_s
        text = 'Welcome to Speed Typing Game'
        if count_s >= len(text):
            count_s = 0
            sliderwords = ''
        sliderwords = sliderwords + text[count_s]
        movingLabel.config(text=sliderwords)
        movingLabel.after(190, slider)
        count_s += 1


    # GUIpart
    root = tkinter.Toplevel()
    root.title('Speed Typing Game')
    root.iconbitmap('Images/icon.ico')
    root.geometry('700x600+400+100')
    root.config(bg='SlateBlue4')
    root.resizable(0, 0)

    # logoImage
    logoImage = PhotoImage(file='Images/clock.png')
    logoLabel = Label(root, image=logoImage, bg='SlateBlue4')
    logoLabel.place(x=220, y=50)

    # movingTextLabel
    movingLabel = Label(root, text='Welcome to Speed Typing Game', bg='SlateBlue4', font=('arial', 25, 'bold'),
                        width=35)
    movingLabel.place(x=0, y=10)
    slider()

    # word_list_Label
    random.shuffle(word_list)
    word_list_Label = Label(root, text=word_list[0], font=('cooper black', 38, 'bold'), bg="SlateBlue4")
    word_list_Label.place(x=350, y=350, anchor=CENTER)

    # wordLabel
    wordLabel = Label(root, text='Words', font=('Castellar', 28, 'bold'), bg="SlateBlue4")
    wordLabel.place(x=30, y=110)

    # countLabel
    countLabel = Label(root, text='0', font=('Castellar', 28, 'bold'), bg="SlateBlue4")
    countLabel.place(x=80, y=180)

    # timeLabel
    timeLabel = Label(root, text='Timer', font=('Castellar', 28, 'bold'), bg="SlateBlue4")
    timeLabel.place(x=510, y=110)

    # time_countLabel
    time_countLabel = Label(root, text='60', font=('Castellar', 28, 'bold'), bg="SlateBlue4")
    time_countLabel.place(x=560, y=180)

    # wordEntry
    wordEntry = Entry(root, font=('arial', 25, 'bold'), bd=6, justify=CENTER)
    wordEntry.place(x=165, y=390)
    wordEntry.focus_set()

    # instructionLabel
    instructionLabel = Label(root, text='Type word and hit Enter', font=('Chiller', 28, 'bold'), bg="SlateBlue4")
    instructionLabel.place(x=210, y=460)

    # importingPics
    poorpic = PhotoImage(file='Images/poor.png')
    goodpic = PhotoImage(file='Images/good.png')
    propic = PhotoImage(file='Images/pro.png')

    # emoji1Label
    emoji1Label = Label(root, bg="SlateBlue4")
    emoji1Label.place(x=80, y=490)

    # emoji2Label
    emoji2Label = Label(root, bg="SlateBlue4")
    emoji2Label.place(x=560, y=490)

    # bind
    root.bind('<Return>', play_game)

    root.mainloop()

def changebg(widget):
    widget.config(bg="wheat4")
    widget.after(100, lambda: widget.config(bg="white"))

def licenses(windows, appVersrion=None):
    width = 500
    height = 480
    win = Toplevel()
    win.wm_title("KeyLearner" + " - License Info")
    screen_width = windows.winfo_screenwidth()
    screen_height = windows.winfo_screenheight()

    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    win.resizable(False, False)
    win.focus_set()
    main_icon = PhotoImage(file="Images/Logo.png")
    win.iconphoto(False, main_icon)
    info_frame = Frame(win, height=60, width=390)
    info_frame.place(x=45, y=5)
    name_lbl = Label(info_frame, text="KeyLearner" + ' - A Typing Tutor App', font=('Helvetica bold', 13))
    name_lbl.place(x=105, y=5)
    version_lbl = Label(info_frame, text=appVersrion)
    version_lbl.place(x=160, y=30)

    line = Frame(win, height=1, width=397, highlightthickness=1, highlightbackground='black')
    line.place(x=40, y=80)

    mit_lbl = Label(win, text='MIT License')
    mit_lbl.place(x=208, y=100)
    copyryt_lbl = Label(win, text='Copyright (c) 2023 Redefined')
    copyryt_lbl.place(x=150, y=115)

    bottom_frame = Frame(win, height=290, width=420)
    bottom_frame.place(x=45, y=145)
    license_text_lbl = Label(bottom_frame,
    text='''Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction. This includes, but is not limited to,
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software. Users who 
receive the Software are permitted to do so, subject to the following conditions:

The above copyright notice and this permission notice must be included in all copies or substantial portions of 
the Software.

THE SOFTWARE IS PROVIDED "AS IS," WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT, OR 
OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

This text covers the terms of use and disclaimers associated with the software, ensuring that users understand their 
rights and responsibilities when using your app.''', justify=LEFT)
    license_text_lbl.place(x=0, y=0)

    close_button = ttk.Button(win, text="Close", command=win.destroy)
    close_button.place(x=205, y=435)

def about(windows):
    width = 500
    height = 500
    win = Toplevel()
    win.wm_title("KeyLearner" + " - About")
    screen_width = windows.winfo_screenwidth()
    screen_height = windows.winfo_screenheight()

    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))

    win.geometry("{}x{}+{}+{}".format(width, height, x, y))
    win.resizable(False, False)
    win.focus_set()
    main_icon = PhotoImage(file="Images/Logo.png")
    win.iconphoto(False, main_icon)

    info_frame = Frame(win, height=165, width=390)
    info_frame.place(x=45, y=15)
    name_lbl = Label(info_frame, text="KeyLearner" + ' - A Typing Tutor App', font=('Helvetica bold', 13))
    name_lbl.place(x=105, y=5)
    version_lbl = Label(info_frame, text='Version 1.0.0')
    version_lbl.place(x=160, y=30)
    line = Frame(win, height=1, width=397, highlightthickness=1, highlightbackground="black")
    line.place(x=49, y=80)

    about_frame = Frame(win, height=230, width=420)
    about_frame.place(x=45, y=100)
    about_lbl = Label(about_frame,
    text='''Welcome to KeyLearner, a Stylish, Powerful, and Fast Typing Tutor designed specifically for Python coding. 
With an elegant user interface, KeyLearner allows you to quickly and easily enhance your Python coding skills. This 
typing tutor app offers comprehensive coverage of Python functions, keywords, and concepts, making it the ideal tool
for anyone looking to excel in Python programming.''',
                      justify=LEFT)
    about_lbl.place(x=0, y=0)

    features_lbl = Label(about_frame, text='Key Features of KeyLearner:: \n\n' \
                          '    - A modern and user-friendly interface tailored for Python coders.\n' \
                          '    - Extensive support for Python functions, keywords, and concepts.\n' \
                        '''    - Access Python resources by typing keywords or functions and 
       seamlessly search Google for additional information.\n''' \
                          '    - Use the speed test mode to test your speed and accuracy of english words', justify=LEFT)
    features_lbl.place(x=0, y=100)

    line1 = Frame(win, height=1, width=397, highlightthickness=1, highlightbackground='black')
    line1.place(x=49, y=340)

    footer_frame = Frame(win, height=60, width=420)
    footer_frame.place(x=45, y=360)
    footer_lbl = Label(footer_frame,
                          text='KeyLearner is a Typing Tutor App  for  Windows. Send  me  the feedbacks,\n'
                               'bug-reports and suggestions about KeyLearner to:', justify=LEFT)
    footer_lbl.place(x=0, y=0)
    email_lbl = Label(footer_frame, text='sanchitpandey263@gmail.com', fg="blue", cursor="hand2")
    email_lbl.place(x=110, y=35)

    close_button = ttk.Button(win, text="Close", command=win.destroy)
    close_button.place(x=210, y=440)

def search():
    searched = search_entry.get()
    url = 'https://www.google.com/search?q={} in python'.format(searched)
    webbrowser.open(url)

################GUI PART
# application window
win = ttkthemes.ThemedTk()
win.title("KeyLearner")
win.get_themes()
win.set_theme("plastik")
win.geometry('1350x760+100+10')
win.resizable(0, 0)

# left panel
left_frame = Frame(win, bg="wheat4", bd=3)
left_frame.place(x=0, y=0)
logo_img = PhotoImage(file="Images/Logo.png")
logo_label = Label(left_frame, image=logo_img, height=100, width=230, bg="wheat4")
logo_label.grid(row=0, column=0)
text_label = Label(left_frame, text="Google search", font={"calibre",12,"black"}, bg="wheat4")
text_label.grid(row=1, column=0, pady=10)
search_entry = Entry(left_frame, width=30)
search_entry.grid(row=2, column=0, pady=15)
search_button = ttk.Button(left_frame, text="Search", command=search)
search_button.grid(row=3, column=0)
empty_label = Label(left_frame, height=4, bg="wheat4")
empty_label.grid(row=4, column=0)

speedtest_Button = Button(left_frame, text="Speed Test", bg="wheat4", fg="white", font={"16"}, activebackground="wheat4", relief=FLAT,
                         width=10, command=lambda: speed_test(win))
speedtest_Button.grid(row=5, column=0, pady=15)
about_Button = Button(left_frame, text="About", bg="wheat4", fg="white", font={"16"}, activebackground="wheat4", relief=FLAT,
                      width=10, command=lambda: about(win))
about_Button.grid(row=6, column=0, pady=15)
licenses_Button = Button(left_frame, text="Licenses", bg="wheat4", fg="white", font={"16"}, activebackground="wheat4", relief=FLAT,
                         width=10, command=lambda: licenses(win))
licenses_Button.grid(row=7, column=0, pady=15)
empty_label_end = Label(left_frame, height=20, bg="wheat4")
empty_label_end.grid(row=8, column=0)

# main frame
main_frame = Frame(win, bd=3)
main_frame.place(x=250, y=0)


# paragraph frame
paragraph_frame = Frame(main_frame)
paragraph_frame.grid(row=0, column=1, pady=5)
paragraph_list = [
'''# Program to generate a random number between 0 and 9
# importing the random module
import random
print(random.randint(0,9))''',
'''friends = ['john', 'pat', 'gary', 'michael']
for i, name in enumerate(friends):
    print ("iteration {iteration} is {name}".format(iteration=i, name=name))''',
'''def greet(name):
    print ('Hello', name)
greet('Jack')
greet('Jill')
greet('Bob')''',
'''parents, babies = (1, 1)
while babies < 100:
    print ('This generation has {0} babies'.format(babies))
    parents, babies = (babies, parents + babies)''',
'''# Python Program to calculate the square root
# Note: change this value for a different result
num = 8 
# To take the input from the user
#num = float(input('Enter a number: '))
num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))''',
'''# Find square root of real or complex numbers
# Importing the complex math module
import cmath
num = 1+2j
# To take input from the user
#num = eval(input('Enter a number: '))
num_sqrt = cmath.sqrt(num)
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))''',
'''name = input("Enter your name: ")
print("Hello, " + name + "!")
print("Nice to meet you.")''',
'''sum = 0
for i in range(1, 6):
    sum += i
print("The sum is", sum)''',
'''s = "Hello, World!"
reversed_s = s[::-1]
print(reversed_s)''',
'''num = 10
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")''',
'''num = 5
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(factorial)''',
'''a, b = 0, 1
for _ in range(5):
    print(a)
    a, b = b, a + b''',
'''numbers = [5, 2, 3, 1, 4]
numbers.sort()
print(numbers)''',
'''numbers = [5, 2, 3, 1, 4]
max_num = max(numbers)
print(max_num)''',
'''numbers = [5, 2, 3, 1, 4]
min_num = min(numbers)
print(min_num)''',
'''numbers = [5, 2, 3, 1, 4]
min_num = min(numbers)
print(min_num)''']
random.shuffle(paragraph_list)
paragraph_label=Label(paragraph_frame, text=paragraph_list[0], wraplength=912, justify=LEFT, font=('arial', 14, 'bold'))
paragraph_label.grid(row=0, column=0)

# text area frame
textarea_frame = Frame(main_frame, bd=4, relief=SUNKEN)
textarea_frame.grid(row=2, column=1)
text_area = Text(textarea_frame, font=("calibre", 15, "bold"), width=80, height=6, bg="mintcream", wrap="word",
                 state=DISABLED)
text_area.grid()

# counter frame
frame_output = Frame(main_frame)
frame_output.grid(row=3, column=1, pady=3)

elapsed_time_label = Label(frame_output, text="Elapsed Time", font=("Tahoma", 15, "bold"), fg="red3")
elapsed_time_label.grid(row=0, column=0, padx=15)

elapsed_timer_label = Label(frame_output, text="0", font=("Tahoma", 15, "bold"))
elapsed_timer_label.grid(row=0, column=1, padx=5)

wpm_label = Label(frame_output, text="CPM", font=("Tahoma", 15, "bold"), fg="red3")
wpm_label.grid(row=0, column=4, padx=15)

wpm_count_label = Label(frame_output, text="0", font=("Tahoma", 15, "bold"))
wpm_count_label.grid(row=0, column=5, padx=5)

accuracy_label = Label(frame_output, text="Accuracy", font=("Tahoma", 15, "bold"), fg="red3")
accuracy_label.grid(row=0, column=6, padx=15)

accuracy_count_label = Label(frame_output, text="0", font=("Tahoma", 15, "bold"))
accuracy_count_label.grid(row=0, column=7, padx=5)

totalwords_label = Label(frame_output, text="Total Characters", font=("Tahoma", 15, "bold"), fg="red3")
totalwords_label.grid(row=0, column=8, padx=15)

totalwords_count_label = Label(frame_output, text="0", font=("Tahoma", 15, "bold"))
totalwords_count_label.grid(row=0, column=9, padx=5)

wrongwords_label = Label(frame_output, text="Wrong Characters", font=("Tahoma", 15, "bold"), fg="red3")
wrongwords_label.grid(row=0, column=10, padx=15)

wrongwords_count_label = Label(frame_output, text="0", font=("Tahoma", 15, "bold"))
wrongwords_count_label.grid(row=0, column=11)

# buttons frame
buttons_frame = Frame(main_frame)
buttons_frame.grid(row=4, column=1, pady=5)

startButton = ttk.Button(buttons_frame, text="Start", width=10, command=start_timer)
startButton.grid(row=0, column=0, padx=35)

submitButton = ttk.Button(buttons_frame, text="Submit", width=10, state=DISABLED, command=count)
submitButton.grid(row=0, column=1, padx=35)

resetButton = ttk.Button(buttons_frame, text="Reset", width=10, state=DISABLED, command=reset)
resetButton.grid(row=0, column=2, padx=35)

exitButton = ttk.Button(buttons_frame, text="Exit", width=10, command=win.destroy)
exitButton.grid(row=0, column=3, padx=35)

# keyboard frame
keyboard_frame = Frame(main_frame, bg="wheat3")
keyboard_frame.grid(row=5, column=1, pady=6)

# number keys
frame1to0 = Frame(keyboard_frame, bg="wheat3")
frame1to0.grid(row=0, column=0, pady=5)

labelbefore1 = Label(frame1to0, text="~\n`", bg="white", fg="black", font=("arial", 13), width=5, height=2,
                     bd=10, relief=GROOVE)
label1 = Label(frame1to0, text="!\n1", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
label2 = Label(frame1to0, text="@\n2", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
label3 = Label(frame1to0, text="#\n3", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
label4 = Label(frame1to0, text="$\n4", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
label5 = Label(frame1to0, text="%\n5", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
label6 = Label(frame1to0, text="^\n6", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
label7 = Label(frame1to0, text="&\n7", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
label8 = Label(frame1to0, text="*\n8", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
label9 = Label(frame1to0, text="(\n9", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
label0 = Label(frame1to0, text=")\n0", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labelafter0 = Label(frame1to0, text="_\n-", bg="white", fg="black", font=("arial", 13), width=5, height=2,
                    bd=10, relief=GROOVE)
label2after0 = Label(frame1to0, text="+\n=", bg="white", fg="black", font=("arial", 13), width=5, height=2,
                     bd=10, relief=GROOVE)
label3after0 = Label(frame1to0, text="backspace", bg="white", fg="black", font=("arial", 13), width=9, height=2,
                     bd=10, relief=GROOVE)

labelbefore1.grid(row=0, column=0, padx=3)
label1.grid(row=0, column=1, padx=3)
label2.grid(row=0, column=2, padx=3)
label3.grid(row=0, column=3, padx=3)
label4.grid(row=0, column=4, padx=3)
label5.grid(row=0, column=5, padx=3)
label6.grid(row=0, column=6, padx=3)
label7.grid(row=0, column=7, padx=3)
label8.grid(row=0, column=8, padx=3)
label9.grid(row=0, column=9, padx=3)
label0.grid(row=0, column=10, padx=3)
labelafter0.grid(row=0, column=11, padx=3)
label2after0.grid(row=0, column=12, padx=3)
label3after0.grid(row=0, column=13, padx=3)

# alphabet keys
frameqtop = Frame(keyboard_frame, bg="wheat3")
frameqtop.grid(row=1, column=0, pady=5)

labeltab = Label(frameqtop, text="tab", bg="white", fg="black", font=("arial", 13), width=9, height=2, bd=10,
                 relief=GROOVE)
labelq = Label(frameqtop, text="Q", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labelw = Label(frameqtop, text="P", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labele = Label(frameqtop, text="E", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labelr = Label(frameqtop, text="R", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labelt = Label(frameqtop, text="T", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labely = Label(frameqtop, text="Y", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labelu = Label(frameqtop, text="U", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labeli = Label(frameqtop, text="I", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labelo = Label(frameqtop, text="O", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labelp = Label(frameqtop, text="P", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labelafterp = Label(frameqtop, text="{\n[", bg="white", fg="black", font=("arial", 13), width=5, height=2,
                    bd=10, relief=GROOVE)
label2afterp = Label(frameqtop, text="}\n]", bg="white", fg="black", font=("arial", 13), width=5, height=2,
                     bd=10, relief=GROOVE)
label3afterp = Label(frameqtop, text="|\n\\", bg="white", fg="black", font=("arial", 13), width=5, height=2,
                     bd=10, relief=GROOVE)

labeltab.grid(row=0, column=0, padx=3)
labelq.grid(row=0, column=1, padx=3)
labelw.grid(row=0, column=2, padx=3)
labele.grid(row=0, column=3, padx=3)
labelr.grid(row=0, column=4, padx=3)
labelt.grid(row=0, column=5, padx=3)
labely.grid(row=0, column=6, padx=3)
labelu.grid(row=0, column=7, padx=3)
labeli.grid(row=0, column=8, padx=3)
labelo.grid(row=0, column=9, padx=3)
labelp.grid(row=0, column=10, padx=3)
labelafterp.grid(row=0, column=11, padx=3)
label2afterp.grid(row=0, column=12, padx=3)
label3afterp.grid(row=0, column=13, padx=3)

frameatol = Frame(keyboard_frame, bg="wheat3")
frameatol.grid(row=2, column=0, pady=5)

labelcapslock = Label(frameatol, text="capslock", bg="white", fg="black", font=("arial", 13), width=11,
                      height=2,
                      bd=10, relief=GROOVE)
labela = Label(frameatol, text="A", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labels = Label(frameatol, text="S", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labeld = Label(frameatol, text="D", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labelf = Label(frameatol, text="F", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labelg = Label(frameatol, text="G", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labelh = Label(frameatol, text="H", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labelj = Label(frameatol, text="J", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labelk = Label(frameatol, text="K", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labell = Label(frameatol, text="L", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labelafterl = Label(frameatol, text=":\n;", bg="white", fg="black", font=("arial", 13), width=5, height=2,
                    bd=10, relief=GROOVE)
label2afterl = Label(frameatol, text="\"\n'", bg="white", fg="black", font=("arial", 13), width=5, height=2,
                     bd=10, relief=GROOVE)
label3afterl = Label(frameatol, text="enter", bg="white", fg="black", font=("arial", 13), width=12, height=2,
                     bd=10, relief=GROOVE)

labelcapslock.grid(row=0, column=0, padx=3)
labela.grid(row=0, column=1, padx=2)
labels.grid(row=0, column=2, padx=3)
labeld.grid(row=0, column=3, padx=3)
labelf.grid(row=0, column=4, padx=3)
labelg.grid(row=0, column=5, padx=3)
labelh.grid(row=0, column=6, padx=3)
labelj.grid(row=0, column=7, padx=3)
labelk.grid(row=0, column=8, padx=3)
labell.grid(row=0, column=9, padx=3)
labelp.grid(row=0, column=10, padx=3)
labelafterl.grid(row=0, column=11, padx=3)
label2afterl.grid(row=0, column=12, padx=3)
label3afterl.grid(row=0, column=13, padx=3)

frameztom = Frame(keyboard_frame, bg="wheat3")
frameztom.grid(row=3, column=0, pady=5)

labelshift = Label(frameztom, text="shift", bg="white", fg="black", font=("arial", 13), width=16, height=2,
                   bd=10, relief=GROOVE)
labelz = Label(frameztom, text="Z", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labelx = Label(frameztom, text="X", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labelc = Label(frameztom, text="C", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labelv = Label(frameztom, text="V", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labelb = Label(frameztom, text="B", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labeln = Label(frameztom, text="N", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labelm = Label(frameztom, text="M", bg="white", fg="black", font=("arial", 13), width=5, height=2, bd=10,
               relief=GROOVE)
labelafterm = Label(frameztom, text="<\n,", bg="white", fg="black", font=("arial", 13), width=5, height=2,
                    bd=10, relief=GROOVE)
label2afterm = Label(frameztom, text=">\n.", bg="white", fg="black", font=("arial", 13), width=5, height=2,
                     bd=10, relief=GROOVE)
label3afterm = Label(frameztom, text="?\n/", bg="white", fg="black", font=("arial", 13), width=5, height=2,
                     bd=10, relief=GROOVE)
label4afterm = Label(frameztom, text="shift", bg="white", fg="black", font=("arial", 13), width=16, height=2,
                     bd=10, relief=GROOVE)

labelshift.grid(row=0, column=0, padx=3)
labelz.grid(row=0, column=1, padx=2)
labelx.grid(row=0, column=2, padx=3)
labelc.grid(row=0, column=3, padx=3)
labelv.grid(row=0, column=4, padx=3)
labelb.grid(row=0, column=5, padx=3)
labeln.grid(row=0, column=6, padx=3)
labelm.grid(row=0, column=7, padx=3)
labelafterm.grid(row=0, column=11, padx=3)
label2afterm.grid(row=0, column=12, padx=3)
label3afterm.grid(row=0, column=13, padx=2)
label4afterm.grid(row=0, column=14, padx=3)

# space bar and other keys
framectrltoctrl = Frame(keyboard_frame, bg="wheat3")
framectrltoctrl.grid(row=4, column=0, pady=5)

labelctrl = Label(framectrltoctrl, text="ctrl", bg="white", fg="black", font=("arial", 13), width=15, height=2,
                  bd=10, relief=GROOVE)
labelalt = Label(framectrltoctrl, text="alt", bg="white", fg="black", font=("arial", 13), width=12, height=2,
                 bd=10, relief=GROOVE)
labelspace = Label(framectrltoctrl, bg="white", fg="black", font=("arial", 13), width=50, height=2, bd=10,
                   relief=GROOVE)
labelalt2 = Label(framectrltoctrl, text="alt", bg="white", fg="black", font=("arial", 13), width=12, height=2,
                  bd=10, relief=GROOVE)
labelctrl2 = Label(framectrltoctrl, text="ctrl", bg="white", fg="black", font=("arial", 13), width=15, height=2,
                   bd=10, relief=GROOVE)

labelctrl.grid(row=0, column=0, padx=3)
labelalt.grid(row=0, column=1, padx=3)
labelspace.grid(row=0, column=2, padx=3)
labelalt2.grid(row=0, column=3, padx=3)
labelctrl2.grid(row=0, column=4, padx=3)

# highlight the key pressed on keyboard
label_numbers = [label1, label2, label3, label4, label5, label6, label7, label8, label9, label0]
label_alphabets = [labela, labelb, labelc, labeld, labele, labelf, labelg, labelh, labeli, labelj, labelk, labell,
                   labelm, labeln, labelo, labelp, labelq, labelr, labels, labelt, labelu, labelv, labelw, labelx,
                   labely, labelz]
label_specialcharacters = [labelbefore1, labelafter0, label2after0, labelafterp, label2afterp, label3afterp, labelafterl
                           , label2afterl, labelafterm, label2afterm, label3afterm, label4afterm]
label_number_specialcharacters = [label1, label2, label3, label4, label5, label6, label7, label8, label9, label0]
label_space = [labelspace]
label_tab = [labeltab]

binding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
binding_capital_alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
binding_small_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
binding_lower_special_characters = ['`', '-', '=', '[', ']', '\\', ';', "'", ',', '.', '/']
binding_upper_special_characters = ['~', '_', '+', '{', '}', '|', ':', '"', '<less>', '>', '?']
binding_number_special_characters = ['!', '@', '#', '$', ' %', '^', '&', '*', '(', ')']

for numbers in range(len(binding_numbers)):
    win.bind(binding_numbers[numbers], lambda event, label=label_numbers[numbers]: changebg(label))

for capital_alphabets in range(len(binding_capital_alphabets)):
    win.bind(binding_capital_alphabets[capital_alphabets],
             lambda event, label=label_alphabets[capital_alphabets]: changebg(label))

for small_alphabets in range(len(binding_small_alphabets)):
    win.bind(binding_small_alphabets[small_alphabets],
             lambda event, label=label_alphabets[small_alphabets]: changebg(label))

for lower_special_characters in range(len(binding_lower_special_characters)):
    win.bind(binding_lower_special_characters[lower_special_characters],
             lambda event, label=label_specialcharacters[lower_special_characters]: changebg(label))

for upper_special_characters in range(len(binding_upper_special_characters)):
    win.bind(binding_upper_special_characters[upper_special_characters],
             lambda event, label=label_specialcharacters[upper_special_characters]: changebg(label))

for number_special_characters in range(len(binding_number_special_characters)):
    win.bind(binding_number_special_characters[number_special_characters],
             lambda event, label=label_number_specialcharacters[number_special_characters]: changebg(label))

win.bind("<space>", lambda event: changebg(labelspace))
win.bind("<Tab>", lambda event: changebg(labeltab))
win.bind("<Return>", lambda event: changebg(label3afterl))
win.bind("<BackSpace>", lambda event: changebg(label3after0))
win.bind("<KeyPress-Caps_Lock>", lambda event: labelcapslock.config(bg="wheat4"))
win.bind("<KeyRelease-Caps_Lock>", lambda event: labelcapslock.config(bg="white"))
win.bind("<Shift_L>", lambda event: changebg(labelshift))
win.bind("<Shift_R>", lambda event: changebg(label4afterm))
win.bind("<Control_L>", lambda event: changebg(labelctrl))
win.bind("<Control_R>", lambda event: changebg(labelctrl2))
win.bind("<Alt_L>", lambda event: changebg(labelalt))
win.bind("<Alt_R>", lambda event: changebg(labelalt2))

win.mainloop()