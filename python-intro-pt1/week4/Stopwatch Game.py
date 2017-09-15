# template for "Stopwatch: The Game"
# http://www.codeskulptor.org/#user43_P7yloxffVC_4.py


# define global variables

import simplegui
import random

width = 300
height = 300

time_count = 0
time_display = ""
win_count = 0
try_count = 0
clock_running = False


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global time_display
    A = t // 600
    B = (t - A * 600) // 100
    C = (t - A * 600 - B * 100) // 10
    D = t % 10
 
    time_display = str(A)+":"+str(B)+str(C)+"."+str(D)
    return time_display
    #print time_display

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global clock_running
    clock_running = True
    timer.start()
    #format(time_count)


def stop():
    timer.stop()
    global clock_running, try_count, win_count
    if clock_running:
        clock_running = False
        try_count += 1
        if time_count % 10 == 0:
            win_count +=1  

def reset():
    global time_count, clock_running, try_count, win_count    
    timer.stop()
    time_count = 0 
    clock_running = False
    try_count = 0
    win_count = 0
    
# define event handler for timer with 0.1 sec interval

def tick():
    global time_count
    time_count += 1
    return time_count
    
# define draw handler
def draw(c):
    global time_display
    c.draw_text(format(time_count), (width//2 - width//6, height//2+height // 10), 36, "white") 
    score = str(win_count)+"/"+str(try_count)
    c.draw_text(score, (width - width // 5, height // 5), 24, "Green")
    
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", width, height)
timer = simplegui.create_timer(100, tick)

# register event handlers
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)

# start frame
frame.start()

# Please remember to review the grading rubric
