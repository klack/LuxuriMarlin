import os
import shutil

def move_files(src_dir, dest_dir, file_exts):
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith(tuple(file_exts)):
                src_file = os.path.join(root, file)
                dest_file = os.path.join(dest_dir, file)
                shutil.move(src_file, dest_file)

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
        os.environ['PLATFORMIO_BUILD_FLAGS'] = self.get_command_flags() + "-DTENLOG_CONFIG=" + self.get_config_name()
        os.environ['PLATFORMIO_BUILD_DIR'] = "./.pio/build/combinations/" + self.get_config_name()
        os.environ['LUXURI_CONFIG_NAME'] = self.get_config_name()
        os.system('pio run --environment BuildCombination')        
    def __init__(self, flags):
        self.flags = flags

# Build a list containing the desired build combinations
list1 = ["TenlogHands2", "TenlogD3", "TenlogD5"]
list2 = ["TMC2208Drivers", "TMC2209Drivers", "A4988Drivers"]
list3 = ["", "BMGExtruder" "HictopTitan"]
list4 = ["", "BLTouchProbe"]
list5 = ["", "MaintainedPowerSwitch"]
list6 = ["", "ManualBedEndstop"]

combinations = [
    (a, b, c, d, e, f ,g) 
    for a in list1 
    for b in list2 
    for c in list3 
    for d in list4 
    for e in list5 
    for f in list6 
]

# Remove empty strings (default configs)
new_combinations = []
for combination in combinations:
    new_combination = [string for string in combination if string != ""]
    new_combinations.append(new_combination)

luxuri_configs = []
for combination in new_combinations:
    luxuri_configs.append(LuxuriConfig(combination))

# Build configs
print(len(luxuri_configs))

i=0
for config in luxuri_configs:
    if(i==5):
        break
    print=(config.get_config_name())
    config.build()
    i+=1

move_files("./.pio/build/combinations/","./.pio/build/",(".hex",".bin"))