from datetime import datetime, date
from ecg_reporter.app.configs import get_config


def add_to_log(row):
    """
    :param row: input row for log
    :return: none
    """
    today = date.today()
    now = str(datetime.now())
    app_path = get_config('app_path')

    logfile = open(app_path + '/log/ecg_reporter_log_{}.txt'.format(str(today)), 'a+')
    logfile.write(str(now) + ': ' + row + '\n')
    logfile.close()