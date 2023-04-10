#
# Generate versions and build numbers
#

import datetime
tm = datetime.datetime.today()

FILENAME_BUILDNO = 'Marlin/Lux_buildno'
FILENAME_VERSION = 'Marlin/Lux_version'
FILENAME_VERSION_H = 'Marlin/Lux_version.h'
build_no = 0
version = ""

try:
    with open(FILENAME_BUILDNO) as f:
        build_no = int(f.readline()) + 1
    with open(FILENAME_VERSION) as f:
        version = f.readline()
except:
    print('Starting build number from 1..')
    build_no = 1

with open(FILENAME_BUILDNO, 'w+') as f:
    f.write(str(build_no))
    print('Build number: {}'.format(build_no))

hf = """
#ifndef BUILD_NUMBER
  #define BUILD_NUMBER "{}"
#endif
#ifndef VERSION
  #define VERSION "{} - {}"
#endif
#ifndef VERSION_SHORT
  #define VERSION_SHORT "{}"
#endif
""".format(build_no, version + "." + str(build_no), datetime.datetime.now(), version + "." + str(build_no))
with open(FILENAME_VERSION_H, 'w+') as f:
    f.write(hf)
