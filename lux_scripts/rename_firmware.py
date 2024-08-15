import os
Import("env")

filename = ""
version = os.environ.get('LUX_VERSION')
build = os.environ.get('LUX_BUILD')
config = os.environ.get('LUX_CONFIG_NAME')

filename = version
# filename += "." + build
filename += "_" + config

env.Replace(PROGNAME="Luxuri_%s" % filename)
