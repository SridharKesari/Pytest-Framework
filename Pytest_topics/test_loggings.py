import logging
# use getLogger()
LOGGER = logging.getLogger(__name__)
def test_myloggings():
    LOGGER.warning('Warning logs')
    LOGGER.error('Error logs')
    LOGGER.critical('Critical logs')
    LOGGER.info('Info logs')
    assert True
