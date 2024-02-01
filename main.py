start_time = 0
stop_time = 0

def on_touch_fwd_button_down():
    fwdMotors.middle_servo.fwd_set_speed(0)
fwdSensors.touch.fwd_on_touch(jacdac.ButtonEvent.DOWN, on_touch_fwd_button_down)

def on_dial1_fwd_dial_turned_direction_ccw(difference):
    fwdMotors.middle_servo.fwd_set_speed(fwdSensors.dial1.fwd_position())
fwdSensors.dial1.fwd_on_dial_turned(fwdSensors.DialDirection.CCW,
    on_dial1_fwd_dial_turned_direction_ccw)

def on_dial1_fwd_dial_turned_direction_cw(difference2):
    fwdMotors.middle_servo.fwd_set_speed(fwdSensors.dial1.fwd_position())
fwdSensors.dial1.fwd_on_dial_turned(fwdSensors.DialDirection.CW,
    on_dial1_fwd_dial_turned_direction_cw)

def on_button_pressed_a():
    global start_time
    start_time = input.running_time()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global stop_time
    stop_time = input.running_time()
    for index in range(2):
        basic.show_number((stop_time - start_time) / 1000)
    basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.B, on_button_pressed_b)
