import inputs
import mouse
import keyboard
# importing dependancies. pyinstaller took care of that for you
x_check = 0
a_check = 0
# these are used for dragging keys.
print("""The controls work as follows:
    - Left Joystick: Cursor movement
    - D-Pad: More precise, but slower cursor movement.
    - Right Joystick: Scrolling
    - Y: Opens Virtual Keyboard on Windows.
    - X: Toggles right mouse button. Press X again to release it.
    - A: Toggles left mouse button. Press A again to release it.
    - B: Switches tabs.
    - Select/Minus: Backspace.
    - Start/Plus: Enter.
    - Left Bumper: Scroll Up
    - Right Bumper: Scroll Down
    - Left Trigger: Right click
    - Right trigger: Left click
    - L3: Open a new tab.
    - R3: Click the mouse wheel.""")
# prints what everything is assigned to
while 1:
    try:
        for event in inputs.get_gamepad():
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
            if event.code == "ABS_X":
                mouse.move(event.state/1000, 0, absolute=False)
            if event.code == "ABS_Y":
                mouse.move(0,event.state/-1000,absolute=False)
            # cursor movement.
            if event.code == "ABS_Z" and event.state == 255:
                mouse.right_click()
            if event.code == "ABS_RZ" and event.state == 255:
                mouse.click()
            if event.code == "BTN_TL" and event.state == 1:
                mouse.wheel()
            if event.code == "BTN_TR" and event.state == 1:
                mouse.wheel(delta=-1)
            if event.code == "ABS_RY":
                mouse.wheel(delta=event.state/10000)
            if event.code == "BTN_WEST" and event.state == 1:
                if x_check == 0:
                    mouse.press('right')
                    x_check = 1
                elif x_check == 1:
                    mouse.release('right')
                    x_check = 0
            if event.code == "BTN_SOUTH" and event.state == 1:
                if a_check == 0:
                    mouse.press('left')
                    a_check = 1
                elif a_check == 1:
                    mouse.release('left')
                    a_check = 0
            # basic mouse functionality.
            if event.code == "BTN_NORTH" and event.state == 1:
                keyboard.send('windows+ctrl+o')
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
            # other stuff that may or may not be useful to the average person
    except inputs.UnpluggedError:
        continue
    # makes it so that the program will not shut down IMMEDIATELY after being unplugged.
