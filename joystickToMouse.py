import inputs
import mouse
import keyboard
# importing dependencies, but pyInstaller took care of that for you
x_check = 0
a_check = 0
# variables, they'll be needed later.
while 1:
    for event in inputs.get_gamepad():
    # gets all the gamepad inputs, and 'event' was just in the documentation, so i used that.
        if event.code == "ABS_HAT0X":
            if event.state == -1:
                mouse.move(-20,0, absolute=False)
            elif event.state == 1:
                mouse.move(20,0, absolute=False)
        if event.code == "ABS_HAT0Y":
            if event.state == -1:
                mouse.move(0,-20,absolute=False)
            elif event.state == 1:
                mouse.move(0,20,absolute=False)
        # Cursor control.        
        if event.code == "ABS_X":
            mouse.move(event.state/1000, 0, absolute=False)
        if event.code == "ABS_Y":
            mouse.move(0,event.state/-1000,absolute=False)
        if event.code == "ABS_Z" and event.state == 255:
            mouse.right_click()
        if event.code == "ABS_RZ" and event.state == 255:
            mouse.click()
        # Using the triggers to show clicks.
        if event.code == "BTN_TL" and event.state == 1:
            mouse.wheel()
        if event.code == "BTN_TR" and event.state == 1:
            mouse.wheel(delta=-1)
        if event.code == "ABS_RY":
            mouse.wheel(delta=event.state/10000)
          # Scrolling, with bumpers OR right joystick.
        if event.code == "BTN_SOUTH" and event.state == 1:
            if a_check == 0:
                mouse.press('left')
                a_check = 1
            elif a_check == 1:
                mouse.release('left')
                a_check = 0
        # dragging.
        if event.code == "BTN_NORTH" and event.state == 1:
            keyboard.send('windows+ctrl+o')
        # Opens virtual keyboard on Windows.
        if event.code == "BTN_EAST" and event.state == 1:
            keyboard.press('alt+tab')
        if event.code == "BTN_SELECT" and event.state == 1:
            keyboard.send("enter")
        if event.code == "BTN_START" and event.state == 1:
            keyboard.send('backspace')
        if event.code == "BTN_THUMBR" and event.state == 1:
            mouse.click('middle')
        if event.code == "BTN_THUMBL" and event.state == 1:
            keyboard.send("ctrl+n")
        # Other stuff.
