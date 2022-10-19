import argparse
import logging


class arguments:
  """ Automated argument handling. """
  def __init__(self, ArgumentList: dict):

    self.parser = argparse.ArgumentParser()

    for argument in ArgumentList.keys()
      argument = ArgumentList[argument]
      self.parser.add_argument(
                                self.Split_Options(argument['options']),
                                help=str(argument['help']),
                                type=argument['class'],
                                action=str(argument['action'])
      )

    self.args = self.parser.parse_args()

  def Split_Options(self, option: str):

    class ImproperOptions(""" The argument string must be a -s:--long
                              POSIX-Style pair of options separated by
                              a colon. """); exit

    try: option.split(":")
    except: raise ImproperOptions


class log:
  """ Logging setup and associated functionality. """

  def __init__( self,
                logfile="./.log": str,
                loglevel=logging.DEBUG: int ):

    logging.basicConfig(filename=logfile, level=loglevel)


  def INFO(msg: str):
    return logging.info(msg)


  def DEBUG(msg: str):
    return logging.debug(msg)


  def ErrorHandling(error):
    return logging.exception("An error was caught:\n{error}\n")


