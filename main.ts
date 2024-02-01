let revolutions = 0
let start = 0
let elapsed_time = 0
let minutes = 0
let RPM = 0
fwdSensors.touch.fwdOnTouch(jacdac.ButtonEvent.Down, function () {
    fwdMotors.middleServo.fwdSetSpeed(0)
    revolutions = 0
    start = control.millis()
})
fwdSensors.dial1.fwdOnDialTurned(fwdSensors.DialDirection.CCW, function (difference) {
    fwdMotors.middleServo.fwdSetSpeed(fwdSensors.dial1.fwdPosition())
})
fwdSensors.dial1.fwdOnDialTurned(fwdSensors.DialDirection.CW, function (difference) {
    fwdMotors.middleServo.fwdSetSpeed(fwdSensors.dial1.fwdPosition())
})
input.onButtonPressed(Button.A, function () {
    basic.showNumber(revolutions)
})
input.onButtonPressed(Button.B, function () {
    elapsed_time = control.millis() - start
    minutes = elapsed_time / 60000
    RPM = revolutions / minutes
    basic.showNumber(RPM)
})
basic.forever(function () {
    if (fwdSensors.touch.fwdIsPressed()) {
        revolutions += 1
        basic.pause(20)
    }
})
