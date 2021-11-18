import datetime
import logging
import os

from features.utils.constants import CHARSET_DECODE

if not os.path.exists('./logs'):
    os.makedirs('logs')

home_dir = os.getcwd()
log_name = 'logs/' + str(datetime.date.today()) + '.log'
log_file = os.path.join(home_dir, log_name)

logging.basicConfig(
    handlers=[logging.FileHandler(filename=log_name, mode='a', encoding=CHARSET_DECODE)],
    level=logging.INFO,
    format='%(asctime)s %(levelname)-6s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

LAYOUT_LOGS = "=" * 100
LAYOUT_LOGS_COMUM = "=" * 70
