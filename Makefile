# IoTEmbedded Project Makefile
# Usage: make setup

.PHONY: all setup copy-temp start-service stop-service

all: copy-temp start-service stop-service
	@echo "All steps complete."

setup:
	@echo "Updating apt and installing sense-hat..."
	sudo apt-get update
	sudo apt-get install -y sense-hat
	@echo "Sense Hat installed successfully"
	@echo "Making sensehat_logger.py executable..."
	chmod +x sensehat_logger.py
	@echo "Creating symlink to /usr/local/bin/sensehat_logger..."
	sudo ln -sf "$(CURDIR)/sensehat_logger.py" /usr/local/bin/sensehat_logger
	@echo "sensehat_logger is now available as a global command."
	@echo "Setting up sensehat_logger systemd service..."
	sudo cp sensehat_logger.service /etc/systemd/system/sensehat_logger.service
	sudo systemctl daemon-reload
	sudo systemctl enable sensehat_logger.service
	sudo systemctl start sensehat_logger.service
	@echo "sensehat_logger service installed and started."
	@echo "Setup complete. Please reboot your device (sudo reboot)"

copy-temp:
	@echo "Creating temp folder and copying sensehat_logger.py..."
	@mkdir -p temp
	@cp sensehat_logger.py temp/
	@echo "sensehat_logger.py copied to temp/ folder."

start-service:
	@echo "Starting sensehat_logger service..."
	sudo systemctl start sensehat_logger.service
	@echo "sensehat_logger service started."

stop-service:
	@echo "Stopping sensehat_logger service..."
	sudo systemctl stop sensehat_logger.service
	@echo "sensehat_logger service stopped."
