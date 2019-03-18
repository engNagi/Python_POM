# TODO Reading the config file from given system Directory

"""
Class to read configuration from test.configuration.ini
"""

import configparser


class ConfigFileReader(configparser.ConfigParser):
	ConfigFile = configparser.ConfigParser()
	ConfigFile.read("test_configuration.ini")
	ConfigSections = ConfigFile.sections()

	def getSubOption (ConfigSections):
			dict = 
		for option in ConfigSections:

			print(option)








