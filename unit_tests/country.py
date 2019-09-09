import logging
import fmcapi
import pprint
pp = pprint.PrettyPrinter(indent=4)


def test__country(fmc):
    logging.info('Testing Country class.')
    obj1 = fmcapi.Country(fmc=fmc)
    logging.info('All Countries -- >')
    result = obj1.get()
    logging.info(result)
    logging.info(f"Total items: {len(result['items'])}")
    del obj1
    obj1 = fmcapi.Country(fmc=fmc, name='Isle Of Man')
    logging.info('One Country -- >')
    logging.info(obj1.get())

    logging.info('Testing Country class done.\n')
