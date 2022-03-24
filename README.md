# Gripper
At the neurobotics lab at University of Waterloo, we are attempting to collect data associated with human grasping actions while picking up of objects (like the ones in the YCB model set). The setup consists of a Reflex_SF gripper (in future also Reflex Takktile) from Righthandrobotics controlled through a Logitech Extreme joystick, an NDI Polaris capturing the coordinates and the quaternion vectors based on rigid body reflectors attached to the Reflex, and an image processing mechanism to capture the position of the YCB object while gripping. 

Control of Reflex_SF: The control of the Reflex_SF is accomplished through sending commands to the 4 Dynamixel servos. A USB2Dynamixel interface is built in to the Reflex_SF. Dynamixel has a detailed instruction set for MX-28, the servo used in Reflex. The actuator protocol description is detailed. An implementation of this interface was made available (see acknowledgement in dynamixel.py).

When calibrating: A black screen will ben shown. Use the (7, 8), (9, 10), (11, 12)
buttons on the joystick to calibrate the 3 gripper fingers. Once the calibration process
is done, press the silver button(2) on the side of the joystick.

After calibration: The black screen will turn white. Push the joystick forward to close the gripper,
backward to open the gripper. Move the joystick left and right will spread or close the 2 parallel fingers.
