/**
 * ***************************************************************************
 * *********************** CONFIGURE YOUR MACHINE HERE ***********************
 * ***************************************************************************
 *
 *   Comment and uncomment lines to match your machine configuration
 *     or visit our Github Releases (https://github.com/klack/LuxuriMarlin/releases) page for precompiled firmare.
 *   Visit our Github Wiki (https://github.com/klack/LuxuriMarlin/wiki) for help identifying parts.
 *
 */

/**
 * Machine Type
 */
// #define TenlogHands2
#define TenlogD3
// #define TenlogD5
// #define TenlogD6

/**
 * Stepper Drivers
 */
// #define A4988Drivers
#define TMC2208Drivers // (Stock most of the time)
// #define TMC2209Drivers
// #define TMC2209ExtrudersOnly //2209 drivers on extruders only

/**
 * Bed Type
 */
#define DCBed //(Stock)
// #define ACBed

/**
 * Bed Endstop
 */
#define OpticalYEndstop // (Stock)
// #define MechanicalYEndstop

/**
 * Power Switch Type
 */
#define MomentaryPowerSwitch // (Stock)
// #define MaintainedPowerSwitch

/**
 * Toolhead
 */
#define NonGearedExtruder // (Stock)
// #define BMGExtruder
// #define HictopTitanExtruder

/**
 * Hotend
 */
#define PFTEHotened // (Stock)
// #define AllMetalHotend

/**
 * Probe
 */
// #define BLTouchProbe
