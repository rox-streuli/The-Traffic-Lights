# TRAFFIC LIGHTS

# Estimated time
# 20-30 minutes
#
# Level of difficulty
# Easy
#
# Objectives
# Learn practical skills related to:
#
#   dealing with Canvas and some of its methods,
#   using different colors.

# Scenario
# Look at the snippet in the editor - can you see that mysterious
# tuple consisting of four three-element tuples? Can you guess what
# information it carries?
#
# It's a set of rules describing the behavior of British-style traffic
# lights. Assume that the very first element of all inner tuples is
# assigned to the red light, the second - to the yellow, and the third -
# to the green one. True means that the light is on, False - off.
#
# As you see, there are four different phases:
#
#   the red light is lit,
#   the red and yellow lights are lit together,
#   the green light is lit,
#   the yellow light is lit.

# Your task is to implement a model which will show how such a
# traffic signal works. The model should look as follows:
#
# As you see, the model is built of three widgets:
#
#   the canvas being a background for all the three lights,

#   the button named "Next" - clicking it switches the signal to the next phase,

#   the button named "Quit" - clicking it immediately exits the program.

# Note: use the phases tuple as a "knowledge base" for your whole code.
# The code has to adopt to any change done to the tuple, e.g., there can
# be more or less than four phases and the lights' combinations can be
# different also.
#
# If traffic lights in your home country work in a different way, you can
# implement your native scheme, but the only change you're allowed to
# make is to modify the phases tuple - the code itself must remain the same.

import tkinter as tk

phases = ((True,  False, False),
          (True,  True,  False),
          (False, False, True),
          (False, True,  False))


def streetlight(y, colour):
    background.create_oval(30, y+30, 105, y+105, outline="black", fill=colour,
                           width=3)


def red_light(on):
    streetlight(0, "red" if on else "gray")


def yellow_light(on):
    streetlight(100, 'yellow' if on else 'gray')


def green_light(on):
    streetlight(200, 'LightGreen' if on else 'gray')


def next_phase():
    global phase
    phase = (phase + 1) % len(phases)
    print(phase)
    red_light(phases[phase][0])
    yellow_light(phases[phase][1])
    green_light(phases[phase][2])


window = tk.Tk()
window.title("Traffic Lights")

background = tk.Canvas(window, width=180, height=350, bg="#555555")
background.grid(row=0, column=0)

next_btn = tk.Button(window, text="Next", command=next_phase)
next_btn.grid(row=1, column=0)

quit_btn = tk.Button(window, text="Quit", command=window.destroy)
quit_btn.grid(row=2, column=0)

phase = -1
next_phase()

window.mainloop()
