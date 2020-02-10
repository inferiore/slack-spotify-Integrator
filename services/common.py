import yaml
import os.path
__config = None

def config():
    global __config
    if not __config:
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "config.yaml")
        with open(path, mode='r') as f:
            __config = yaml.load(f,Loader=yaml.FullLoader)
    return __config