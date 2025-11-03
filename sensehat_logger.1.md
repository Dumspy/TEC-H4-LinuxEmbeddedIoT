---
title: Sense Hat Logger
section: 1
header: User Manual
footer: Sense Hat Logger
date: November 3, 2025
---

# sensehat_logger(1) — Sense HAT Temperature & Humidity Display

## NAME
sensehat_logger — display temperature or humidity on the Sense HAT LED matrix

## SYNOPSIS
**sensehat_logger** [**-p** temp|fugt]

## DESCRIPTION
**sensehat_logger** is a Python utility for Raspberry Pi Sense HAT that displays either temperature or humidity readings on the LED matrix. The display mode can be toggled using the Sense HAT joystick. The script can be run manually or as a systemd service.

- Temperature readings are shown in degrees Celsius.
- Humidity readings are shown as a percentage.
- Joystick controls allow you to rotate the display and switch between modes.

## OPTIONS
- **-p temp**   Display temperature (default)
- **-p fugt**   Display humidity

## JOYSTICK CONTROLS
- **Up**: Rotate display to 0°
- **Right**: Rotate display to 90°
- **Down**: Rotate display to 180°
- **Left**: Rotate display to 270°
- **Middle**: Toggle between temperature and humidity display

## EXAMPLES
Display temperature (default):
    sensehat_logger

Display humidity:
    sensehat_logger -p fugt

## INSTALLATION
To install and set up **sensehat_logger** as a global command and systemd service:

    make setup

This will:
- Update apt and install the sense-hat pandoc packages
- Make sensehat_logger.py executable
- Create a symlink at /usr/local/bin/sensehat_logger
- Install and start the systemd service

## SERVICE MANAGEMENT
Start the service:
    make start-service

Stop the service:
    make stop-service

## FILES
- sensehat_logger.py         Main script
- sensehat_logger.service    Systemd service file
- Makefile                   Build and setup instructions

---
This README is formatted for use as a man page. For manual installation or troubleshooting, see the Makefile and comments in sensehat_logger.py.
