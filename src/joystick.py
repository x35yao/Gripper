__author__ = 'srkiyengar'
# Significant joystick code or the basis of it comes from pygame.joystick sample code
import pygame



JOY_DEADZONE_A0 = 0.2
JOY_DEADZONE_A1 = 0.1
MOVE_TICKS = 15
MOVE_TICKS_SERVO4 = 10

# Before invoking this class pygame.init() needs to be called


class ExtremeProJoystick():
    def __init__( self):
        # Initialize the joysticks
        pygame.joystick.init()
        self.joystick_count = pygame.joystick.get_count()
        if self.joystick_count == 0:
            raise RuntimeError('No Joystick not found\n')
        else:
            My_joystick = pygame.joystick.Joystick(0)
            name = My_joystick.get_name()
            if ("Logitech Extreme 3D" in name):
                self.name = name
                My_joystick.init()
                self.axes = My_joystick.get_numaxes()
                self.buttons = My_joystick.get_numbuttons()
                self.hats = My_joystick.get_numhats()
                self.joystick= My_joystick
                self.min_val = [-JOY_DEADZONE_A0,-JOY_DEADZONE_A1,-0.5,-0.5]
                self.max_val = [JOY_DEADZONE_A0,JOY_DEADZONE_A1,0.5,0.5]
            else:
                raise RuntimeError('Logitech Extreme #D Joystick not found\n')


    def get_axis_displacement_and_grip(self,k):
        """
        This function has to get the displacement of the Logitech Extreme #D Joystick axis (there are 4 of which 0 and 1
        are used to determine servo movement. Axis 0 is used to move servo 4 to change the separation between fingers 1
        and 2 while Axis 1 displacement determines the aperture of the Reflex (meaning servos 1, 2 and 3 are rotated by the
        same measure in either directions"
        :param k is the Axis identifier:
        :return: is a tuple move, how much, and which direction. The move = 1 means aperture change move = 2 is finger
        separation. moveby is based on one circle being equal to 4096. This is an offset. The direction determines opening
        or closing.
        """
        displacement = self.joystick.get_axis(k)
        move = 0
        move_by = 0
        direction = 0
        if displacement > 0:
            if displacement > self.max_val[k]:
                direction = 1
                if k == 1:
                    move = 1
                    move_by= int(displacement*MOVE_TICKS)
                elif k == 0:
                    move = 2
                    move_by = int(displacement*MOVE_TICKS_SERVO4)
                elif k == 2:
                    pass
                elif k == 3:
                    pass
            else:
                pass    #ignore deadzone
        elif displacement < 0:
            if displacement < self.min_val[k]:
                direction = -1
                if k == 1:
                    move = 1
                    move_by = int(abs(displacement)*MOVE_TICKS)
                elif k == 0:
                    move = 2
                    move_by = int(abs(displacement)*MOVE_TICKS_SERVO4)
                elif k == 2:
                    pass
                elif k == 3:
                    pass
            else:
                pass
        return move,move_by,direction

    def get_button_pressed(self, my_event):
        button_number = my_event.dict['button']    # from pygame.event
        return button_number

    def get_button_released(self, my_event):
        button_number = my_event.dict['button']    # from pygame.event
        return button_number

    def get_hat_movement(self,my_event):
        Hat = my_event.dict['value']
        if Hat[0] < 0:
            return "R"  #Right
        if Hat[0] > 0:
            return "L"  #Left
        if Hat[1] < 0:
            return "U"  #Up
        if Hat[1] > 0:
            return "D"  #Down

        return "E"      #No movement


