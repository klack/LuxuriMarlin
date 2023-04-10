import os

# Build a list containing the desired build combinations
list1 = ["TenlogHands2", "TenlogD3", "TenlogD5"]
list2 = ["TMC2208Drivers", "TMC2209Drivers", "A4988Drivers"]
list3 = ["", "ACBed"]
list4 = ["", "ManualBedEndstop"]
list5 = ["", "MaintainedPowerSwitch"]
list6 = ["", "BLTouchProbe"]
list7 = ["", "HictopTitan"]
list8 = ["", "AllMetalHotend"]

combinations = [
    (a, b, c, d, e, f ,g) 
    for a in list1 
    for b in list2 
    for c in list3 
    for d in list4 
    for e in list5 
    for f in list6 
    for g in list7
]

print(len(combinations))

# Remove empty strings (default configs)
new_combinations = []
for combination in combinations:
    new_combination = [string for string in combination if string != ""]
    new_combinations.append(new_combination)

class LuxuriConfig:
    flags = []
    def get_config_name(self):
        get_config_name = ''
        for string in self.flags:
            get_config_name += (string + "_")
        return get_config_name[:-1] # Remove trailing _
    def get_command_flags(self):
        get_command_flags = ''
        for string in self.flags:
            get_command_flags += ("-D" + string + " ")
        return get_command_flags
    def build(self): # Run the build command with the appropriate environment variables
        os.environ['PLATFORMIO_BUILD_FLAGS'] = self.get_command_flags()
        os.environ['PLATFORMIO_BUILD_DIR'] = "./.pio/build/combinations/" + self.get_config_name()
        os.environ['LUXURI_FIRMWARE_NAME'] = self.get_config_name()
        os.system('pio run --environment BuildCombination')        
    def __init__(self, flags):
        self.flags = flags

luxuri_configs = []
for combination in new_combinations:
    luxuri_configs.append(LuxuriConfig(combination))

for config in luxuri_configs:
    # print(config.get_config_name())
    # print(config.get_command_flags())
    config.build()

# luxuri_configs[0].build()

# SET PLATFORMIO_BUILD_FLAGS=-DTENLOG_CONFIG="AutoBuild" -DMY_TENLOG -DMaintainedPowerSwitch
# os.system("C:\Users\rlayt\.platformio\penv\Scripts\platformio.exe run --environment My_Tenlog -t upload")
# os.environ['PLATFORMIO_BUILD_FLAGS'] = '-DTENLOG_CONFIG="AutoBuildBbby" -DTenlogHands2 -DMaintainedPowerSwitch -DTMC2208Drivers -DACBed -DHictopTitan -DAllMetalHotend -DBLTouchProbe -DMaintainedPowerSwitch'
# os.system('C:\\Users\\rlayt\\.platformio\\penv\\Scripts\\platformio.exe run --environment BuildCombinations')

# C:\Users\rlayt\.platformio\penv\Scripts\platformio.exe run --environment My_Tenlog -t upload
# How to set the current pio env?