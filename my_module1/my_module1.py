#! /usr/bin/env python    # Create shebang line
'''
Module-level doc-string goes here.
'''

# Module metadata goes here.
__author__ = 'Nexus J. Xi'

# Use absolute path over relative
import sys
# from x import y

# MODULE CONSTANTS
USE_ONLY_UPPERCASE = 'constant1'

# Setup global variables here, such as
# session_to_app1 = requests.Session()

# Setup Logger, Handler, and Formatter
# logger = logging.getLogger(__name__)
# rotate_file_handler = RotatingFileHandler(kwargs**)    # Maybe I should consider storing log to system log folder, such as /var/log/
# formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
# Assemble Logger
# rotate_file_handler.setFormatter(formatter)
# logger.addHandler(rotate_file_handler)
# logger.setLevel(logging.INFO)


class MyModule1(object):
    '''
    Class-level doc-string.
    '''
    
    def __init__(self, *args, **kwargs):
        '''
        Function-level doc-string.
        '''
        pass

if __name__ == '__main__':
    pass