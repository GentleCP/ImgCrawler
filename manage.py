# @Author  : GentleCP
# @Email   : 574881148@qq.com
# @File    : manage.py
# @Item    : PyCharm
# @Time    : 2020-04-21 13:45
# @WebSite : https://www.gentlecp.com

import sys
import logging
from core.netbian import netbian
from settings import SAVE_PATH,URLS_DICT


if __name__ == '__main__':
    if sys.argv[1] == 'netbian':
        try:
            netbian(type = sys.argv[2], base_url=URLS_DICT['netbian'],
                    save_pwd=SAVE_PATH)
        except IndexError:
            netbian(base_url=URLS_DICT['netbian'], save_pwd=SAVE_PATH)
    else:
        logging.error('Sorry, your operation is not permitted.')