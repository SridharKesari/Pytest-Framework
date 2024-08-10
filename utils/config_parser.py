import configparser
import pathlib
from configparser import ConfigParser
from pathlib import Path

cfgFile = 'pets_qa.ini'
cfgFileDir = 'config'
cfgFileFlaskApp = 'apiserverqa.ini'

# config = ConfigParser()  # import configparser then use configparser.ConfigParser()

BASE_DIR = Path(__file__).resolve().parent.parent  # import pathlib then use pathlib.Path(__file__)
print(BASE_DIR)  # D:\PythonWorkspace\Pytest-Framework
CONFIG_FILE = BASE_DIR.joinpath(cfgFileDir).joinpath(cfgFile)
print(CONFIG_FILE)  # D:\PythonWorkspace\Pytest-Framework\config\pets_qa.ini
CONFIG_FILE_FLASKAPP = BASE_DIR.joinpath(cfgFileDir).joinpath(cfgFileFlaskApp)

config = ConfigParser()
config.read(CONFIG_FILE)  # read the config file

configFlaskApp = ConfigParser()
configFlaskApp.read(CONFIG_FILE_FLASKAPP)


def getPetAPIURL():
    return config['pet']['url']  # use config variable and access the config info present in the pets_qa.ini file


def getStoreAPIURL():
    return config['store']['url']


def getFlaskAppBaseURL():
    baseURL = 'http://' + configFlaskApp['flaskapp']['url'] + ':' + configFlaskApp['flaskapp']['port'] + '/api/'
    return baseURL


print(getPetAPIURL())
print(getStoreAPIURL())
print(getFlaskAppBaseURL())


def getSridharDetails():
    return config['sridhar']['wife'] + config['sridhar']['son'] + config['sridhar']['daughter']


print(getSridharDetails())
