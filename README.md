# brain-text

How to use:
- Cut positive lead connecting battery pack and main circuit board
- Connect incoming wire to GND
- Connect pin D1 to wire to 10 ohm resistor, then red LED then to wire connecting to board(all in series)
- Upload switchTurn.ino to first NodeMCU
- Connect negative lead to GND pin on second NodeMCU
- Run wire from T pin on neurosky chip to RX pin(GPIO 3)
- Upload testBrain.ino to second NodeMCU(be sure to disconnect from RX first, won't upload correctly otherwise)
