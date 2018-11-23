#!/usr/bin/env python3
import time
from ev3dev2.motor import LargeMotor, OUTPUT_C, OUTPUT_B, SpeedPercent, MoveTank

def main():
    time.sleep(2)
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    tank_drive.on_for_seconds(SpeedPercent(100), SpeedPercent(100), 3)

if __name__ == '__main__':
    main()