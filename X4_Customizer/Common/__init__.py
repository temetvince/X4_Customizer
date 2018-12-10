'''
Holds modules that will be commonly imported by transforms.
'''
# Import exceptions early, due to some dependency issues.
from .Exceptions import File_Missing_Exception
from .Exceptions import Obj_Patch_Exception
from .Exceptions import Text_Patch_Exception
from .Exceptions import Gzip_Exception
from .Exceptions import XML_Patch_Exception
# Provide easy access to a few functions/class/modules.
from .Settings import Settings
from .Logs import Transform_Log
from .Logs import Customizer_Log_class
from .Transform_Manager import Transform_Wrapper
from .Transform_Manager import Transform_Was_Run_Before
#from .Settings import Set_Path