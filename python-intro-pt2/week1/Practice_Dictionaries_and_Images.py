###################################################
###################################################
# 1  Create a dictionary 𝚍𝚊𝚢_𝚝𝚘_𝚗𝚞𝚖𝚋𝚎𝚛 that converts the days of the week "𝚂𝚞𝚗𝚍𝚊𝚢", "𝙼𝚘𝚗𝚍𝚊𝚢", … into the numbers 𝟶, 𝟷, …, respectively. 
# http://www.codeskulptor.org/#user43_4HE9HT1eXn_0.py

# Day to number dictionary problem

###################################################
# Student should enter code below

day_to_number = {"Sunday": 0, "Monday": 1, "Tuesday": 2,
                "Wednesday": 3, "Thursday": 4, "Friday": 5,
                "Saturday": 6}

###################################################
# Test data

print day_to_number["Sunday"]
print day_to_number["Monday"]
print day_to_number["Tuesday"]
print day_to_number["Wednesday"]
print day_to_number["Thursday"]
print day_to_number["Friday"]
print day_to_number["Saturday"]



###################################################
###################################################
# 2  Create dictionary for 𝚗𝚊𝚖𝚎_𝚕𝚘𝚘𝚔𝚞𝚙 that, when you lookup the keys "𝙹𝚘𝚎", "𝚂𝚌𝚘𝚝𝚝", "𝙹𝚘𝚑𝚗", and "𝚂𝚝𝚎𝚙𝚑𝚎𝚗", you get the values "𝚆𝚊𝚛𝚛𝚎𝚗", "𝚁𝚒𝚡𝚗𝚎𝚛", "𝙶𝚛𝚎𝚒𝚗𝚎𝚛", and "𝚆𝚘𝚗𝚐", respectively.
# http://www.codeskulptor.org/#user43_kak9MoTTcs_1.py

# Day to number dictionary problem

###################################################
# Student should enter code below

name_lookup = {"Joe": "Warren", "Scott": "Rixner", 
               "John": "Greiner", "Stephen": "Wong"}

###################################################
# Test data

print name_lookup["Joe"]
print name_lookup["Scott"]
print name_lookup["John"]
print name_lookup["Stephen"]



###################################################
###################################################
# 3  Debug the program template below so that the resulting program draws the supplied image on the canvas. 
# http://www.codeskulptor.org/#user43_0ZwMXXhzoe_0.py

# Image debugging problem

###################################################
# Student should enter code below

import simplegui

# load test image
test_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/Race-Car.png")
test_image_size = [135, 164]
test_image_center = [test_image_size[0] / 2, test_image_size[1] / 2]

# draw handler
def draw(canvas):
    canvas.draw_image(test_image, test_image_center, test_image_size, 
                      test_image_center, test_image_size)

# create frame and register draw handler    
frame = simplegui.create_frame("Test image", test_image_size[0], test_image_size[1])
frame.set_draw_handler(draw)

# start frame
frame.start()



###################################################
###################################################
# 4  Load this image of an asteroid, and draw the image centered at the last mouse click. Prior to any mouse clicks, the image should be drawn in the middle of the canvas. The image size is 95×93 pixels. 
# http://www.codeskulptor.org/#user43_e60FWmoWJ3_0.py

# Image positioning problem

###################################################
# Student should enter code below

import simplegui

# global constants
WIDTH = 400
HEIGHT = 300
click_pos = [WIDTH / 2, HEIGHT / 2]

# load test image
test_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid.png")
test_image_size = [95, 93]
test_image_center = [test_image_size[0] / 2, test_image_size[1] / 2]


# mouseclick handler
def click(pos):
    global click_pos
    click_pos = pos
    
# draw handler
def draw(canvas):
    canvas.draw_image(test_image, test_image_center, test_image_size, 
                      click_pos, test_image_size)
    
# create frame and register draw handler    
frame = simplegui.create_frame("Test image", WIDTH, HEIGHT)
frame.set_canvas_background("Gray")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)    

# start frame
frame.start()                                       



###################################################
###################################################
# 5  Challenge: Find an image of your choosing, and upload it to an image sharing site such as imgur.com. Add a direct link to the image to a CodeSkulptor program and write a program that draws the image on the canvas.
# For this last problem, we will not provide a template. However, we note that common problems in this process include:

# Having the image URL point to a webpage instead of an image,
# Choosing an image sharing site that has restrictions on the number of downloads or,
# Using 𝚐𝚎𝚝_𝚠𝚒𝚍𝚝𝚑() and 𝚐𝚎𝚝_𝚑𝚎𝚒𝚐𝚑𝚝() to compute the image size before the image has loaded. These calls return an image size of zero which results in an error in 𝚍𝚛𝚊𝚠_𝚒𝚖𝚊𝚐𝚎. To fix this error, you should either hard code the image size or use an 𝚒𝚏 statement prevent the call to 𝚍𝚛𝚊𝚠_𝚒𝚖𝚊𝚐𝚎 until the image sizes are not zero (indicating the image has loaded).
# One recommendation for testing for whether your image loading code is working correctly is to email the CodeSkulptor URL for your program to another computer and test whether the image load works on the new computer. Web browsers often cache images locally which may cause your program to run on the computer where the code was developed, but not work on other machines. This test is highly recommend if you decide to use images in Memory.