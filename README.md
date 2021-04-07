# brain-text

Hardware:
- Force trainer: https://www.amazon.ca/Science-Trainer-Brain-Sensing-Hologram-Electronic/dp/B00X5CCDYQ
- NodeMCU(x2): https://amzn.to/2WkOtPx

How to use:
- Cut positive lead connecting battery pack and main circuit board
- Connect incoming wire to GND
- Connect pin D1 to wire to 10 ohm resistor, then red LED then to wire connecting to board(all in series)
- Upload switchTurn.ino to first NodeMCU
- Connect negative lead to GND pin on second NodeMCU
- Run wire from T pin on neurosky chip to RX pin(GPIO 3)
- Upload testBrain.ino to second NodeMCU(be sure to disconnect from RX first, won't upload correctly otherwise)

Python:
- Install matplotlib, twilio and pyserial with pip3
- Create free twilio account: https://www.twilio.com/docs/usage/tutorials/how-to-use-your-free-trial-account
- Replace ACCNT_SID and ACCNT_TOKEN in repData.py with your account SID and TOKEN(available on dashboard)
- Replace TWILIO_PHONE_NUMBER with number associated with your account(also available on dashboard)
- Replace RECIPIENT_PHONE_NUMBER with the phone number of intended recipiend, formatted as '+1XXXXXXXXXX'
- Connect first NodeMCU to external USB power source(not laptop)
- Connect second NOdeMCU to laptop over USB
- Turn on headset and run repData.py
