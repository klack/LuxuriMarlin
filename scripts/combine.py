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

# Generate a list of build flags from the combinations
build_flag_list = []
for combination in new_combinations:
    build_flags = ''
    for string in combination:
        build_flags += ("-D" + string + " ")
    build_flag_list.append(build_flags)

# Run the build command with the appropriate environment variables
i=0
for build_flags in build_flag_list:
    print(build_flags)
    os.environ['PLATFORMIO_BUILD_FLAGS'] = build_flags
    os.environ['PLATFORMIO_BUILD_DIR'] = "D:\\Temp\\" + str(i +"\\"
    os.system('pio run --environment BuildCombination')
    i+=1

    
# SET PLATFORMIO_BUILD_FLAGS=-DTENLOG_CONFIG="AutoBuild" -DMY_TENLOG -DMaintainedPowerSwitch
# os.system("C:\Users\rlayt\.platformio\penv\Scripts\platformio.exe run --environment My_Tenlog -t upload")
# os.environ['PLATFORMIO_BUILD_FLAGS'] = '-DTENLOG_CONFIG="AutoBuildBbby" -DTenlogHands2 -DMaintainedPowerSwitch -DTMC2208Drivers -DACBed -DHictopTitan -DAllMetalHotend -DBLTouchProbe -DMaintainedPowerSwitch'
# os.system('C:\\Users\\rlayt\\.platformio\\penv\\Scripts\\platformio.exe run --environment BuildCombinations')

# C:\Users\rlayt\.platformio\penv\Scripts\platformio.exe run --environment My_Tenlog -t upload
# How to set the current pio env?