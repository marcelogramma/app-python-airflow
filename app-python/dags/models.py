from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import configinc as config

DB_CONFIG_DICT = config.conn_dic

DB_CONN_FORMAT = config.conn_db

DB_CONN_URI_DEFAULT = DB_CONN_FORMAT.format(
    database=config.DB_NAME_BASE, **DB_CONFIG_DICT
)

engine_default = create_engine(DB_CONN_URI_DEFAULT)

NEW_DB_NAME = config.DB_NAME

DB_CONN_URI_NEW = DB_CONN_FORMAT.format(database=NEW_DB_NAME, **DB_CONFIG_DICT)


def setup_module():
    conn = engine_default.connect()
    conn.execute("COMMIT")
    # Do not substitute user-supplied database names here.
    conn.execute("CREATE DATABASE %s" % NEW_DB_NAME)
    conn.close()


if __name__ == "__main__":
    setup_module()
