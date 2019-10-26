# -*- coding: iso-8859-1 -*-
#*===========================================================================*#
#*                                                                           *#
#* File     : eMaksPower-steering-system-WOBIT                               *#
#*                                                                           *#
#* Project  : mPLC                                                           *#
#* System   : MPU2                                                           *#
#* Version  : 1.00                                                           *#
#* Company  : Ko³o Naukowe Robotyków                                         *#
#*                                                                           *#
#* Author   : Hubert Graczyk / Piotr Saffarini                               *#
#* Date     : 17.09.2019                                                     *#
#*===========================================================================*#

DefUserVar(name="x_dir", value = 1, descr ="", min_value=0x00, max_value =0xFFFF)# X DIR - 0x5101.01h
DefUserVar(name="x_axis_value", value = 0, descr ="", min_value=0x0, max_value =0xFFFF)# X Joy position - 0x5101.02h

DefUserVar(name="y_dir", value = 1, descr ="", min_value=0x00, max_value =0xFFFF)# Y DIR - 0x5102.01h
DefUserVar(name="y_axis_value", value = 0, descr ="", min_value=0x0, max_value =0xFFFF)# Y Joy position - 0x5102.02h

DefUserVar(name="x_precent_value", value = 0, descr ="", min_value=0x0, max_value =0xFF)# X Joy position in precentage scale - 0x5103.01h
DefUserVar(name="y_precent_value", value = 0, descr ="", min_value=0x0, max_value =0xFF)# Y Joy position in precentage scale - 0x5103.02h

# Configuration Init  -----------------------------------------------------------
def InitPars():
   Sp(0x3004, 0x00, 0)                # DEV_Enable - Disable
   Sp(0x3000, 0x00, 0x1)              # DEV_Cmd - Clear error
   Sp(0x3000, 0x00, 0x82)             # DEV_Cmd - Default parameter

   Sp(0x3221, 0x00, 10000)            # CURR_LimitMaxPos
   Sp(0x3223, 0x00, 10000)            # CURR_LimitMaxNeg
   Sp(0x3224, 0x01, 10000)            # CURR_DynLimitPeak
   Sp(0x3224, 0x02, 5000)             # CURR_DynLimitCont

   Sp(0x3240, 0x00, 10000)            # CURR_Acc_dI
   Sp(0x3241, 0x00, 10000)            # CURR_Acc_dT
   Sp(0x3242, 0x00, 10000)            # CURR_Dec_dI
   Sp(0x3243, 0x00, 100)              # CURR_Dec_dT
   Sp(0x3244, 0x00, 40000)            # CURR_Dec_QuickStop_dI
   Sp(0x3245, 0x00, 50)               # CURR_Dec_QuickStop_dT

   Sp(0x324C, 0x00, 1)                # CURR_RampType

   Sp(0x3350, 0x00, 0x94A)            # VEL_Feedback

   Sp(0x3550, 0x00, 0x94A)            # SVEL_Feedback

   Sp(0x3830, 0x00, 32000)            # PWM_Frequency

   Sp(0x3900, 0x00, 1)                # MOTOR_Type
   Sp(0x3901, 0x00, 3000)             # MOTOR_Nn
   Sp(0x3902, 0x00, 48000)            # MOTOR_Un

   Sp(0x3910, 0x00, 8)                # MOTOR_PolN
   Sp(0x3911, 0x00, 2)                # MOTOR_Polarity

   Sp(0x3962, 0x00, 2000)             # MOTOR_ENC_Resolution

   # Movement parameters ------------------------------------------------------
   Sp(0x3003, 0x00, 7)                # DEV_Mode - POS mode
   Sp(0x3720, 0x00, -250)             # POS_PositionLimitMin - lower limit = -250 ink
   Sp(0x3720, 0x01, 250)              # POS_PositionLimitMax - upper limit = 250 ink
   #Sp(0x3762, 0x00, 0)               # POS_ActualPosition - set postion to 0

   Sp(0x3321, 0x00, 1500)             # VEL_LimitMaxPos - pos. limit = 1500
   Sp(0x3323, 0x00, 1500)             # VEL_LimitMaxNeg - neg. limit = 1500
   Sp(0x3304, 0x00, 0x0300)           # Enable Velocity from 0x3300 value
   Sp(0x3300, 0x00, 100)              # Set Velocity = 100 RPM
   Sp(0x334C, 0x00, 0)                # Deactivate the ramp generator

   '''
   Sp(0x334C, 0x00, 1)                # Activate the ramp generator
   Sp(0x3340, 0x00, 2000)             # Acceleration_dV = 2000 RPM
   Sp(0x3341, 0x00, 100)              # Acceleration_dT = 100 s
   Sp(0x3342, 0x00, 1000)             # Deceleration_dV = 1000 RPM
   Sp(0x3343, 0x00, 200)              # Deceleration_dT = 200 s
   '''

   Sp(0x3004, 0x00, 1)                # DEV_Enable - Enable

# Configuration of CAN frames -------------------------------------------------

   Sp(0x2011, 0x02, 1684107116)       # ...tion - Default parameter communication
   Sp(0x2011, 0x05, 1684107116)       # DS2000_RestoreD...000 - Default parameter

# ===== RX CAN CONFIG ===== #
   Sp(0x1400, 0x01, 0xC000021D)       # COP_RxPDO1_CommunicationParameter_CobId
   Sp(0x1400, 0x01, 0x4000021D)       # COP_RxPDO1_CommunicationParameter_CobId

   Sp(0x1401, 0x01, 0xC000022D)       # COP_RxPDO2_CommunicationParameter_CobId
   Sp(0x1401, 0x01, 0x4000022D)       # COP_RxPDO2_CommunicationParameter_CobId

   Sp(0x1402, 0x01, 0xC000030D)       # COP_RxPDO3_CommunicationParameter_CobId
   Sp(0x1402, 0x01, 0x4000030D)       # COP_RxPDO3_CommunicationParameter_CobId

# ===== RX FRAME DATA ===== #
   #0x21D - AXIS X                                                                  
   Sp(0x1600, 0x00, 0x0)              # Disable mapping                             
   Sp(0x1600, 0x01, 0x51010210)       # object 0: JOY_ADC_X AXIS Value % (2 bytes)  
   Sp(0x1600, 0x02, 0x51010110)       # object 1: DIR: 1-Forward, 0-Rear (2 byte)   
   Sp(0x1600, 0x00, 0x2)              # Enable mapping with 3 objects               
                                                                                    
   #0x22D - AXIS Y                                                                  
   Sp(0x1601, 0x00, 0x0)              # Disable mapping                             
   Sp(0x1601, 0x01, 0x51020210)       # object 0: JOY_ADC_Y AXIS Value % (2 bytes)  
   Sp(0x1601, 0x02, 0x51020110)       # object 1: DIR: 1-Forward, 0-Rear (2 byte)   
   Sp(0x1601, 0x00, 0x2)              # Enable mapping with 3 objects               

   #0x30D - LEDs State
   Sp(0x1602, 0x00, 0x0)              # Disable mapping
   Sp(0x1602, 0x01, 0x31580008)       # object 0: LED Enable (1 bytes)
   Sp(0x1602, 0x02, 0x31580108)       # object 1: LED State (1 bytes)
   Sp(0x1602, 0x00, 0x2)              # Enable mapping with 2 objects

   # ===== TX CAN CONFIG ===== #
   Sp(0x1800, 0x01, 0xC000031D)       # COP_TxPDO1_CommunicationParameter_CobId
   Sp(0x1800, 0x01, 0x4000031D)       # COP_TxPDO1_CommunicationParameter_CobId

   Sp(0x1801, 0x01, 0xC000032D)       # COP_TxPDO2_CommunicationParameter_CobId
   Sp(0x1801, 0x01, 0x4000032D)       # COP_TxPDO2_CommunicationParameter_CobId

   Sp(0x1802, 0x01, 0xC000033D)       # COP_TxPDO3_CommunicationParameter_CobId
   Sp(0x1802, 0x01, 0x4000033D)       # COP_TxPDO3_CommunicationParameter_CobId

   Sp(0x1803, 0x01, 0xC000034D)       # COP_TxPDO4_CommunicationParameter_CobId
   Sp(0x1803, 0x01, 0x4000034D)       # COP_TxPDO4_CommunicationParameter_CobId


   # ===== TX FRAME DATA ===== #
   #0x31D
   Sp(0x1A00, 0x00, 0x0)              # Disable mapping
   Sp(0x1A00, 0x01, 0x31100020)       # object 0: Electronic Voltage [mV](4 bytes)
   Sp(0x1A00, 0x02, 0x31110020)       # object 1: Power Voltage [mV](4 bytes)
   Sp(0x1A00, 0x00, 0x2)              # Enable mapping with 2 objects

   #0x32D
   Sp(0x1A01, 0x00, 0x0)              # Disable mapping
   Sp(0x1A01, 0x01, 0x31120020)       # object 0: Motor Voltage [mV] (4 bytes)
   Sp(0x1A01, 0x02, 0x31130020)       # object 1: Motor Current [mA] (4 bytes)
   Sp(0x1A01, 0x00, 0x2)              # Enable mapping with 2 objects

   #0x33D
   Sp(0x1A02, 0x00, 0x0)              # Disable mapping
   Sp(0x1A02, 0x01, 0x31140010)       # object 0: Electronic Temperature (2 bytes)
   Sp(0x1A02, 0x00, 0x1)              # Enable mapping with 1 objects

   #0x34D
   Sp(0x1A03, 0x00, 0x0)              # Disable mapping
   Sp(0x1A03, 0x01, 0x33620020)       # object 0: Actual Velocity (4 bytes)
   Sp(0x1A03, 0x02, 0x37620020)       # object 1: Actual Motor Position (4 bytes)
   Sp(0x1A03, 0x00, 0x2)              # Enable mapping with 2 objects


# Main program ================================================================
InitPars()
Sp(0x2040,0x02,5)                     # NMT communication Enable

# Main loop -------------------------------------------------------------------
while 1:   
   y_precent_value = (y_axis_value*128)/65535  #precentage conversion

   if(y_dir == 1):
     Sp(0x3790, 0x00,((y_precent_value) * Gp(0x3720, 0x01)/100))

   elif(y_dir == 0):
     Sp(0x3790, 0x00,((y_precent_value) * Gp(0x3720, 0x00)/100))




