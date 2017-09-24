# Implementation of classic arcade game Pong
# http://www.codeskulptor.org/#user43_pxYLaKesJJQlIsv_2.py

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
width = 600
height = 400       
ball_radius = 20
pad_width = 8
pad_height = 80
half_pad_width = pad_width / 2
half_pad_height = pad_height / 2
left = False
right = True

#paddles
#paddle1_pos = height / 2.5
#paddle2_pos = height / 2.5
#paddle1_vel = 0
#paddle2_vel = 0
paddle_vel = 5
#
#ball_pos = [width / 2, height / 2]
#ball_vel = [0, 1] # pixels per update (1/60 seconds)

ball_pos = [width / 2, height / 2]

paddle2_vel = [0,0]
paddle1_vel = [0,0]
ball_vel = [(random.randrange(120, 240) / 60),-(random.randrange(60, 180) / 60)]

paddle1_pos = [pad_width/2, height/2-pad_height/2]
paddle2_pos = [width-pad_width/2, height/2-pad_height/2]

score1 = 0
score2 = 0


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel, paddle2_vel, paddle1_vel, paddle1_pos, paddle2_pos # these are vectors stored as lists
    
    ball_pos = [width / 2, height / 2]
    paddle2_vel = [0,0]
    paddle1_vel = [0,0]
    paddle1_pos = [pad_width/2, height/2-pad_height/2]
    paddle2_pos = [width-pad_width/2, height/2-pad_height/2]
        
    if right: 
        ball_vel = [(random.randrange(120, 240) / 60),-(random.randrange(60, 180) / 60)]
    else: 
        ball_vel = [-(random.randrange(120, 240) / 60),-(random.randrange(60, 180) / 60)]

        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    global ball_pos
    
    ball_pos = [width / 2, height / 2]
    paddle1_pos = [pad_width/2, height/2-pad_height/2]
    paddle2_pos = [width-pad_width/2, height/2-pad_height/2]
    score1 = 0
    score2 = 0
    ball_vel = [(random.randrange(120, 240) / 60),-(random.randrange(60, 180) / 60)]

    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos 
    global paddle1_vel, paddle2_vel, ball_pos, ball_vel, right, ball_radius
    global pad_width, pad_height
    
    # draw mid line and gutters
    canvas.draw_line([width / 2, 0],[width / 2, height], 1, "White")
    canvas.draw_line([pad_width, 0],[pad_width, height], 1, "White")
    canvas.draw_line([width - pad_width, 0],[width - pad_width, height], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, ball_radius, 2, "Red", "White")
        
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[1] = paddle1_pos[1] + paddle1_vel[1]
    paddle2_pos[1] = paddle2_pos[1] + paddle2_vel[1]
    
    # make sure the paddles do not move beyond vertical limits
    if paddle1_pos[1] <= 0 or paddle1_pos[1] >= height-pad_height: 
        paddle1_vel[1] = 0
    
    if paddle2_pos[1] <= 0 or paddle2_pos[1] >= height-pad_height: 
        paddle2_vel[1] = 0

    # check if the ball is touching the upper/bottom bounderies - reflect
    if ball_pos[1] <= ball_radius or ball_pos[1] >= (height -1 - ball_radius):
        ball_vel[1] = - ball_vel[1]

    # Check if the ball hits a left/right paddle and reflect
    # Make sure to account for PAD_WIDTH from both directions, if the ball is in the gutter
    if (ball_pos[0]+ball_radius) >= (width-pad_width) and ball_pos[1] >=paddle2_pos[1] and ball_pos[1] <= (paddle2_pos[1]+pad_height):
        ball_vel[0] = - ball_vel[0]*1.1
    elif ball_pos[0] <= ball_radius+pad_width and ball_pos[1] >=paddle1_pos[1] and ball_pos[1] <= (paddle1_pos[1]+pad_height):
        ball_vel[0] = - ball_vel[0]*1.1
    elif ball_pos[0] < (ball_radius) or ball_pos[0] > (width - ball_radius): 
        if ball_pos[0] > width/2: 
            score1 += 1
            right = False
        else: 
            score2 +=1
            right = True
        ball_vel[0] = 0
        ball_vel[1] = 0
        spawn_ball(right) 
    
    # draw paddles
    canvas.draw_line (paddle1_pos, [paddle1_pos[0], paddle1_pos[1]+pad_height], pad_width, "White")
    canvas.draw_line (paddle2_pos, [paddle2_pos[0], paddle2_pos[1]+pad_height], pad_width, "White")
    # draw scores
    canvas.draw_text (str(score1), [100, 50], 40, 'White')
    canvas.draw_text (str(score2), [500, 50], 40, 'White')
    
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle_vel
        
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1] += paddle_vel
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel[1] -= paddle_vel
    elif key==simplegui.KEY_MAP["s"]: 
        paddle1_vel[1] += paddle_vel
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel[1] -= paddle_vel
        
def keyup(key):
    global paddle1_vel, paddle2_vel, paddle_vel
    
    if key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 0
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = 0
    elif key==simplegui.KEY_MAP["s"]: 
        paddle1_vel[1] = 0
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = 0

# create frame
frame = simplegui.create_frame("Pong", width, height)
button1 = frame.add_button('Restart', new_game)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
frame.start()