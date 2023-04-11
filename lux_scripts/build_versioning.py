#
# Generate versions and build numbers
#
import os
import datetime
tm = datetime.datetime.today()

FILENAME_VERSION = 'Marlin/Lux_version'
FILENAME_VERSION_H = 'Marlin\src\inc\Lux_version.h'
version = ""
build_no = 0
build_date = ""

try:
    with open(FILENAME_VERSION) as f:
        version = f.readline()
        build_no = int(f.readline())
        build_date = f.readline()
except:
    print('Could not find version information')
    build_no = 1
    version = ""

if(os.environ.get('LUX_INCREMENT_BUILD') == "1"):
  build_no+=1
  build_date = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}"

with open(FILENAME_VERSION, 'w+') as f:
    f.writelines([version,str(build_no),build_date])
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
""".format(build_no, version, str(build_no), date, version)
with open(FILENAME_VERSION_H, 'w+') as f:
    f.write(hf)
