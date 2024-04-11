#Constant file

#Here we just want to return my config.yaml file and params.yaml
#Instead of hardcoding this  path everytime
#We set the path here and use it every single time

from pathlib import Path

CONFIG_FILE_PATH =Path("config/config.yaml")
PARAMS_FILE_PATH =Path("params.yaml")
