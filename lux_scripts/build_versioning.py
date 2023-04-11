#
# Generate versions and build numbers
#
import os
import datetime
tm = datetime.datetime.today()

FILENAME_VERSION = 'Marlin\src\inc\Lux_version'
FILENAME_VERSION_H = 'Marlin\src\inc\Lux_version.h'
version = ""
build_no = 0
build_date = ""

try:
    with open(FILENAME_VERSION) as f:
        version = f.readline().strip()
        build_no = int(f.readline())
        build_date = f.readline().strip()
except:
    print('Could not find version information')
    build_no = 1
    version = "1"

if not (os.environ.get('LUX_SKIP_INCREMENT') == "1"):
    build_no+=1
    build_date = f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}"

os.environ['LUXURI_VERSION'] = version
os.environ['LUXURI_BUILD'] = str(build_no)
    
with open(FILENAME_VERSION, 'w+') as f:
    f.write(version + "\n")
    f.write(str(build_no) + "\n")
    f.write(build_date + "\n")
    print('Build number: {}'.format(build_no))

hf = """#ifndef BUILD_NUMBER
  #define BUILD_NUMBER "{}"
#endif
#ifndef DETAILED_BUILD_VERSION
  #define DETAILED_BUILD_VERSION "{} build {} {}"
#endif
#ifndef SHORT_BUILD_VERSION
  #define SHORT_BUILD_VERSION "{}"
#endif
""".format(build_no, version, str(build_no), build_date, version)
with open(FILENAME_VERSION_H, 'w+') as f:
    f.write(hf)
