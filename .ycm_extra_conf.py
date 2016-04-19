# https://github.com/Valloric/ycmd/blob/master/cpp/ycm/.ycm_extra_conf.py

def FlagsForFile(filename, **kwargs):
    return {
        'flags': ['-std=c++11',
                  '-isystem',
                  '-Iinclude',
                  '-Isource',
                  '-Wall',
                  '-Wextra',
                  '-Weverything',
                  '-pedantic'],
        'do_cache': True
    }

