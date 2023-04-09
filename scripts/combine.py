list1 = ["TenlogHands2", "TenlogD3", "TenlogD5"]
list2 = ["", "ACBed"]
list3 = ["", "ManualBedEndstop"]
list4 = ["", "MaintainedPowerSwitch"]
list5 = ["", "BLTouchProbe"]
list6 = ["", "HictopTitan"]
list7 = ["", "AllMetalHotend"]

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
# print(combinations)

new_combinations = []
for combination in combinations:
    new_combination = [string for string in combination if string != ""]
    new_combinations.append(new_combination)

for combination in new_combinations:
    new_string = ''
    for string in combination:
        new_string += ("-D" + string + " ")
    print(new_string)

# print(new_combinations)
# print(f"-D{new_combinations[56][0]} -D{new_combinations[56][1]}")
# ['TenlogHands2', 'ACBed', 'ManualBedEndstop', 'MaintainedPowerSwitch']
# -DTenlogHnads2 -DACBed -DManualBedEndstop -DMaintainedPowerSwitch