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
#* Date     : 18.08.2019                                                     *#
#*===========================================================================*#


# Configuration Init  -----------------------------------------------------------
def InitPars():
   Sp(0x3004, 0x00, 0)                # DEV_Enable - Disable
   Sp(0x3000, 0x00, 0x1)              # DEV_Cmd - Clear error
   Sp(0x3000, 0x00, 0x82)             # DEV_Cmd - Default parameter

   Sp(0x3221, 0x00, 40000)            # CURR_LimitMaxPos
   Sp(0x3223, 0x00, 40000)            # CURR_LimitMaxNeg
   Sp(0x3224, 0x01, 40000)            # CURR_DynLimitPeak
   Sp(0x3224, 0x02, 40000)            # CURR_DynLimitCont

   Sp(0x3240, 0x00, 40000)            # CURR_Acc_dI
   Sp(0x3241, 0x00, 40000)            # CURR_Acc_dT
   Sp(0x3242, 0x00, 40000)            # CURR_Dec_dI
   Sp(0x3243, 0x00, 10)               # CURR_Dec_dT
   Sp(0x3244, 0x00, 40000)            # CURR_Dec_QuickStop_dI
   Sp(0x3245, 0x00, 2)                # CURR_Dec_QuickStop_dT

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

# Configuration of CAN frames -------------------------------------------------
   
   Sp(0x2011, 0x02, 1684107116)       # ...tion - Default parameter communication
   Sp(0x2011, 0x05, 1684107116)       # DS2000_RestoreD...000 - Default parameter
    
    
   # ===== RX CAN CONFIG ===== #
   Sp(0x1400, 0x01, 0xC0000D40)       # COP_RxPDO1_CommunicationParameter_CobId
   Sp(0x1400, 0x01, 0x40000D40)       # COP_RxPDO1_CommunicationParameter_CobId 
   
   Sp(0x1401, 0x01, 0xC0000D41)       # COP_RxPDO2_CommunicationParameter_CobId
   Sp(0x1401, 0x01, 0x40000D41)       # COP_RxPDO2_CommunicationParameter_CobId
   
   Sp(0x1402, 0x01, 0xC0000D42)       # COP_RxPDO3_CommunicationParameter_CobId
   Sp(0x1402, 0x01, 0x40000D42)       # COP_RxPDO3_CommunicationParameter_CobId
   
   # ===== RX FRAME DATA ===== #        
   #0xD40
   Sp(0x1600, 0x00, 0x0)              # Disable mapping
   Sp(0x1600, 0x01, 0x31580108)       # object 0: LED State (1 bytes)
   Sp(0x1600, 0x02, 0x33000020)       # object 1: Desired Velocity (4 bytes)
   Sp(0x1600, 0x00, 0x2)              # Enable mapping with 2 objects   
   
   #0xD41
   Sp(0x1601, 0x00, 0x0)              # Disable mapping
   Sp(0x1601, 0x01, 0x33400020)       # object 0: Acceleration dV(4 bytes)
   Sp(0x1601, 0x02, 0x33410020)       # object 1: Acceleration dT(4 bytes)
   Sp(0x1601, 0x00, 0x2)              # Enable mapping with 2 objects  
   
   #0xD42
   Sp(0x1602, 0x00, 0x0)              # Disable mapping
   Sp(0x1602, 0x01, 0x37620020)       # object 0: Acctual Position(4 bytes)
   Sp(0x1602, 0x02, 0x37900020)       # object 1: Absolute move(4 bytes)
   Sp(0x1602, 0x00, 0x2)              # Enable mapping with 2 objects
   
   # ===== TX CAN CONFIG ===== #
   Sp(0x1800, 0x01, 0xC0000D20)       # COP_TxPDO1_CommunicationParameter_CobId
   Sp(0x1800, 0x01, 0x40000D20)       # COP_TxPDO1_CommunicationParameter_CobId 
   
   Sp(0x1801, 0x01, 0xC0000D21)       # COP_TxPDO2_CommunicationParameter_CobId
   Sp(0x1801, 0x01, 0x40000D21)       # COP_TxPDO2_CommunicationParameter_CobId 
   
   Sp(0x1802, 0x01, 0xC0000D22)       # COP_TxPDO3_CommunicationParameter_CobId
   Sp(0x1802, 0x01, 0x40000D22)       # COP_TxPDO3_CommunicationParameter_CobId 
   
   Sp(0x1803, 0x01, 0x80000000)       # COP_TxPDO4_CommunicationParameter_CobId
   Sp(0x1803, 0x01, 0x80000000)       # COP_TxPDO4_CommunicationParameter_CobId  
   
   # ===== TX FRAME DATA ===== #  
   #0xD20
   Sp(0x1A00, 0x00, 0x0)              # Disable mapping                     
   Sp(0x1A00, 0x01, 0x31100020)       # object 0: Electronic Voltage [mV](4 bytes) 
   Sp(0x1A00, 0x02, 0x31110020)       # object 1: Power Voltage [mV](4 bytes)    
   Sp(0x1A00, 0x00, 0x2)              # Enable mapping with 2 objects       
   
   #0xD21
   Sp(0x1A01, 0x00, 0x0)              # Disable mapping
   Sp(0x1A01, 0x01, 0x31120020)       # object 0: Motor Voltage [mV] (4 bytes)
   Sp(0x1A01, 0x02, 0x31130020)       # object 0: Motor Current [mA] (4 bytes)
   Sp(0x1A01, 0x00, 0x2)              # Enable mapping with 2 objects  
   
   #0xD22
   Sp(0x1A02, 0x00, 0x0)              # Disable mapping
   Sp(0x1A02, 0x01, 0x31140010)       # object 0: Electronic Temperature (2 bytes)
   Sp(0x1A02, 0x00, 0x1)              # Enable mapping with 1 objects   
   
           
# Main program ================================================================
InitPars()

# Main loop -------------------------------------------------------------------
while 1:          