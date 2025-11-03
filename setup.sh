sudo apt-get update
sudo apt-get install sense-hat

echo "Sense Hat installed successfully"
echo "Setup complete"

# Make sensehat_logger.py executable
chmod +x sensehat_logger.py

# Symlink to /usr/local/bin
sudo ln -sf "$(pwd)/sensehat_logger.py" /usr/local/bin/sensehat_logger

echo "sensehat_logger is now available as a global command."
echo "Please reboot your device (sudo reboot)"
