import sys
import yaml
import re

from typing import (
    Optional,
    List,
    cast
)

from JsKell.repl import (
    start_repl,
    read_module    
)


_JsKell_: str = """ 
                                                .         .                                                
     

    99999 9      d888888o.      888888     88888888   888888'888   888888 888
    99999 9    .`8888:' `88.    888888     88888888   888888'888   888888 888
    99999 99   8.`8888.   Y8    888888     88888888   888888'888   888888 888
    '99999 9    `8.`8888.       8888888   888888888   888888'888   888888 888
     '99999 9    `8.`8888.      8888888888888888      888888'888   888888 888
      '9999 9      8.`8888.     99998888888888        888888'888   888888 888
8b     9999 9  8b   `8.`8888.   99999999999999        888888'888   888888 888 
'9b    ,999 9  `8b.  ;8.`8888   9999999  9999999      988888'888   888888 888  
 `Y8888P ,88P  `Y8888P ,88P'    99999     99999999    888889'999   999999 999
"""



def show_cover(version):
    global _JsKell_
    print('-'*106)
    print(
        f'\n\nWelcome to  v{version}, the Program Language of the future for the Programming Functional and a lot more\n\n{_JsKell_}')
    print('-'*106)


def show_head(version):
    print(f'JsKell v{version} | Exit: exit() | Update: update()')


def get_configs():
    with open('configs.yaml', 'r') as fin:
        configs = yaml.load(fin, Loader=yaml.FullLoader)
    return dict(configs)


def presentation_config(configs, params, exe_file=False):
    version = configs['version']
    if not params is None:
        if exe_file:
            if '-cover' in params:
                show_cover(version)
                return
            show_head(version)
        else:
            if not '-ncover' in params:
                show_cover(version)
                return
            show_head(version)
    else:
        if exe_file:
            show_head(version)
        else:
            show_cover(version)




def main(path=None, params=None) -> None:
    configs = get_configs()
    if not params is None and '-version' in params:
        version = configs['version']
        print(f'JsKell v{version}')
        return
    if path is None:
        presentation_config(configs, params, exe_file=False)
        start_repl()
    elif not path is None:
        presentation_config(configs, params, exe_file=True)

        src = read_module(path)
        if not src is None:
            start_repl(src, path)


def filter_path_params(args):
    path = list(filter(lambda s: not re.match('(\S+?\.sf$)', s) is None, args))
    params = list(filter(lambda s: s.startswith('-'), args))
    if len(path) > 0:
        path = path[0]
    else:
        path = None

    if len(params) == 0:
        params = None

    return path, params


if __name__ == '__main__':
    args: List[str] = sys.argv

    if len(args) > 1:
        path, params = filter_path_params(args)
    else:
        path, params = None, None
    try:
        main(path, params)
    except KeyboardInterrupt:
        print('\n↳ Good bye \n')
