#
# Generate versions and build numbers
#
import os
import datetime
tm = datetime.datetime.today()

FILENAME_BUILDNO = 'Marlin/Lux_buildno'
FILENAME_VERSION = 'Marlin/Lux_version'
FILENAME_VERSION_H = 'Marlin\src\inc\Lux_version.h'
build_no = 0
version = ""

try:
    with open(FILENAME_BUILDNO) as f:
        build_no = int(f.readline())
    with open(FILENAME_VERSION) as f:
        version = f.readline()
except:
    print('Could not find version information')
    build_no = 1
    version = 1

if(os.environ['LUX_INCREMENT_BUILD'] == "1"):
  build_no+=1

with open(FILENAME_BUILDNO, 'w+') as f:
    f.write(str(build_no))
    print('Build number: {}'.format(build_no))

hf = """
#ifndef BUILD_NUMBER
  #define BUILD_NUMBER "{}"
#endif
#ifndef DETAILED_BUILD_VERSION
  #define DETAILED_BUILD_VERSION "{} build {} {}"
#endif
#ifndef SHORT_BUILD_VERSION
  #define SHORT_BUILD_VERSION "{}"
#endif
""".format(build_no, version, str(build_no), f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}", version)
with open(FILENAME_VERSION_H, 'w+') as f:
    f.write(hf)
