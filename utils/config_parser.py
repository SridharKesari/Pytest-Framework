import configparser
import pathlib
from configparser import ConfigParser
from pathlib import Path

cfgFile = 'pets_qa.ini'
cfgFileDir = 'config'

# config = ConfigParser()  # import configparser then use configparser.ConfigParser()

BASE_DIR = Path(__file__).resolve().parent.parent  # import pathlib then use pathlib.Path(__file__)
print(BASE_DIR)
CONFIG_FILE = BASE_DIR.joinpath(cfgFileDir).joinpath(cfgFile)
print(CONFIG_FILE)

config = ConfigParser()
# read the config file
config.read(CONFIG_FILE)


def getPetAPIURL():
    return config['pet']['url']  # use config variable and access the config info present in the pets_qa.ini file


def getStoreAPIURL():
    return config['store']['url']


print(getPetAPIURL())
print(getStoreAPIURL())


def getSridharDetails():
    return config['sridhar']['wife'] + config['sridhar']['son'] + config['sridhar']['daughter']


print(getSridharDetails())
