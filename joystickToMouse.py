import inputs
import mouse
import keyboard
while 1:
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
            keyboard.press('Page Up')
            keyboard.release('Page Up')
        if event.code == "BTN_SOUTH" and event.state == 1:
            keyboard.press('Page Down')
            keyboard.release('Page Down')
        if event.code == "BTN_NORTH" and event.state == 1:
            keyboard.send('windows+ctrl+o')
        if event.code == "BTN_EAST" and event.state == 1:
            keyboard.press('alt+tab')
        if event.code == "BTN_SELECT" and event.state == 1:
            keyboard.send("enter")
        if event.code == "BTN_START" and event.state == 1:
            keyboard.send('backspace')
