/**
 * ***************************************************************************
 * ******************************* DO NOT EDIT *******************************
 * ***************************************************************************
 *
 *   Configure your base machine in Configuration_MyTenlog.h
 *   Then edit Configuration.adv and Configuration.h directly if needed.
 *
 */

//Machine Type
#if ENABLED(TenlogHands2)
  #define LUX_X_BED_SIZE 235
  #define LUX_Y_BED_SIZE 240
  #define LUX_X_MIN_POS -47
  #define LUX_X_MAX_POS  LUX_X_BED_SIZE
  #define LUX_X2_MIN_POS 15
  #define LUX_X2_MAX_POS 279
  #define LUX_Y_MAX_POS 240
  #define LUX_Z_MAX_POS 260
#elif ENABLED(TenlogD3)
  #define LUX_X_BED_SIZE 310
  #define LUX_Y_BED_SIZE 310
  #define LUX_X_MIN_POS -47
  #define LUX_X_MAX_POS  LUX_X_BED_SIZE
  #define LUX_X2_MIN_POS 15
  #define LUX_X2_MAX_POS 359
  #define LUX_Y_MAX_POS 333
  #define LUX_Z_MAX_POS 350
#elif ENABLED(TenlogD5)
  #define LUX_X_BED_SIZE 505
  #define LUX_Y_BED_SIZE 520
  #define LUX_X_MIN_POS -47
  #define LUX_X_MAX_POS  LUX_X_BED_SIZE
  #define LUX_X2_MIN_POS 15
  #define LUX_X2_MAX_POS 554
  #define LUX_Y_MAX_POS 533
  #define LUX_Z_MAX_POS 610
#elif ENABLED(TenlogD6)
  #define LUX_X_BED_SIZE 605
  #define LUX_Y_BED_SIZE 620
  #define LUX_X_MIN_POS -47
  #define LUX_X_MAX_POS  LUX_X_BED_SIZE  
  #define LUX_X2_MIN_POS 15
  #define LUX_X2_MAX_POS 654
  #define LUX_Y_MAX_POS 633
  #define LUX_Z_MAX_POS 610
#endif

//Bed Type
#if ENABLED(ACBed)
  #define LUX_TEMP_SENSOR_BED 11
  #define LUX_BED_MAXTEMP 120
#else //DC Bed
  #define LUX_TEMP_SENSOR_BED 1
  #define LUX_BED_MAXTEMP 90
#endif

//Bed Endstop
#if ENABLED(LeafSwitchEndstop)
  #define LUX_Y_MIN_ENDSTOP_INVERTING false
#else //Optical Y
  #define LUX_Y_MIN_ENDSTOP_INVERTING true
#endif

//Power Switch Type
//  No logic needed here

//Toolhead
#if ENABLED(TenlogBMGToolhead)||ENABLED(BMGSuperVolcano)||ENABLED(BMGExtruderV2)||ENABLED(BMGExtruderV3)
  #define LUX_DEFAULT_AXIS_STEPS_PER_UNIT { 80, 80, 800, 415, 415 }
#elif ENABLED(HictopTitan)
  #define LUX_DEFAULT_AXIS_STEPS_PER_UNIT { 80, 80, 800, 382.17, 382.17 }
#elif ENABLED(BMGExtruder)
  #define LUX_DEFAULT_AXIS_STEPS_PER_UNIT { 80, 80, 800, 413, 413 }
#else // Stock Toolhead
  #define LUX_DEFAULT_AXIS_STEPS_PER_UNIT { 80, 80, 800, 92.6, 92.6 }
#endif

#if ENABLED(HictopTitan) && ENABLED(TenlogD3)
  #define LUX_DEFAULT_DUPLICATION_X_OFFSET 142
#elif ENABLED(TenlogHands2)
  #define LUX_DEFAULT_DUPLICATION_X_OFFSET 115
#elif ENABLED(TenlogD3)
  #define LUX_DEFAULT_DUPLICATION_X_OFFSET 155
#elif ENABLED(TenlogD5)
  #define LUX_DEFAULT_DUPLICATION_X_OFFSET 250
#elif ENABLED(TenlogD6)
  #define LUX_DEFAULT_DUPLICATION_X_OFFSET 305
#endif

#if ENABLED(AllMetalHotend)
  #define LUX_HEATER_0_MAXTEMP 310
  #define LUX_HEATER_1_MAXTEMP 310
#else
  #define LUX_HEATER_0_MAXTEMP 255
  #define LUX_HEATER_1_MAXTEMP 255
#endif

//Filament Sensor
#define LUX_NUM_RUNOUT_SENSORS 1

//Probe
#if ENABLED(BLTouchProbe)
  #define LUX_AUTO_BED_LEVELING_UBL 1
  #define LUX_BABYSTEP_ZPROBE_OFFSET 1
  #define LUX_BLTOUCH 1
  #define LUX_MIN_SOFTWARE_ENDSTOP_Z 0
  #define LUX_Z_MIN_PROBE_USES_Z_MIN_ENDSTOP_PIN 1
  #define LUX_Z_MIN_PROBE_REPEATABILITY_TEST 1
  #define LUX_Z_MIN_ENDSTOP_INVERTING false
  #define LUX_Z_STEPPER_AUTO_ALIGN 1
  #define LUX_NOZZLE_TO_PROBE_OFFSET { 7, -47, -1.34 }
  #define LUX_PROBING_MARGIN_BACK 30
  #define LUX_Z_SAFE_HOMING 1
  #define LUX_Z_MIN_PROBE_USES_Z_MIN_ENDSTOP_PIN 1
  #define UBL_DEVEL_DEBUGGING //Broken, throwing ubl error in g28
#else //No probe
  #define LUX_MESH_BED_LEVELING 1
  #define LUX_MIN_SOFTWARE_ENDSTOP_Z 1
  #define LUX_USE_ZMAX_PLUG 1
  #define LUX_Z_MULTI_ENDSTOPS 1
  #define LUX_Z_MIN_ENDSTOP_INVERTING true
  #define LUX_PROBING_MARGIN_BACK PROBING_MARGIN
  #define BABYSTEP_HOTEND_Z_OFFSET 1
#endif

//Stepper Drivers
#if ENABLED(TMC2208Drivers)
  #define LUX_XYZ_DRIVER_TYPE TMC2208_STANDALONE
  #define LUX_INVERT_X_DIR false
  #define LUX_INVERT_Y_DIR true
  #define LUX_INVERT_Z_DIR false
  #define LUX_INVERT_E0_DIR true
  #if ENABLED(HictopTitan)
    #define LUX_INVERT_E1_DIR true
  #else
    #define LUX_INVERT_E1_DIR false
	#endif
  #define LUX_LIN_ADVANCE 1
#elif ENABLED(TMC2209Drivers)
  #define LUX_XYZ_DRIVER_TYPE TMC2209_STANDALONE
  #define LUX_INVERT_X_DIR false
  #define LUX_INVERT_Y_DIR true
  #define LUX_INVERT_Z_DIR false
  #define LUX_INVERT_E0_DIR true
  #if ENABLED(HictopTitan)
    #define LUX_INVERT_E1_DIR true
  #else
    #define LUX_INVERT_E1_DIR false
	#endif
  #define LUX_LIN_ADVANCE 1
#elif ENABLED(A4988Drivers)
  #define LUX_XYZ_DRIVER_TYPE A4988
  #define LUX_INVERT_X_DIR true
  #define LUX_INVERT_Y_DIR false
  #define LUX_INVERT_Z_DIR true
  #define LUX_INVERT_E0_DIR false
  #if ENABLED(HictopTitan)
    #define LUX_INVERT_E1_DIR false
  #else
    #define LUX_INVERT_E1_DIR true
	#endif
  #define LUX_LIN_ADVANCE 1
#endif
#if ENABLED(TMC2209ExtrudersOnly) //2209 drivers on extruders only
  #undef LUX_LIN_ADVANCE
  #undef LUX_INVERT_E0_DIR
  #undef LUX_INVERT_E1_DIR
  #define LUX_E_DRIVER_TYPE TMC2209_STANDALONE
  #define LUX_INVERT_E0_DIR true
  #if ENABLED(HictopTitan)
    #define LUX_INVERT_E1_DIR true
  #else
    #define LUX_INVERT_E1_DIR false
  #endif
  #define LUX_LIN_ADVANCE 1
#else
  #define LUX_E_DRIVER_TYPE LUX_XYZ_DRIVER_TYPE
#endif

//Required Flags
#define HAS_STATUS_MESSAGE 1 //M117 Support without a screen
#define SAFETY_Z_UNPARK 4.00 //Avoid bed clips (Height to raise. Set to 0 for disable). Murdock 26/04/2021
#define SAFETY_Y_UNPARK 15.00 //Avoid bed clips (Distance to move on Y axis for avoid bed clips). Murdock 26/04/2021