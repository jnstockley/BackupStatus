import datetime

import config.config as config
from config.sql_config import setup_db_connection, save, get_all
from models.models import Folder


def main():
    config.load_config()
    config.set_profile()
    setup_db_connection()
    test = Folder(path="hello",
                  friendly_name="world",
                  last_update=datetime.datetime.now())
    save(test)
    get_all()
    #print(type(config.get_value("servers.server")))


if __name__ == '__main__':
    main()
