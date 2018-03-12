from pysimplesoap.client import SoapClient
from suds.client import Client
from pysimplesoap.simplexml import SimpleXMLElement
from prestapyt.prestapyt import PrestaShopWebServiceError, PrestaShopWebService, PrestaShopWebServiceDict
from xml.etree import ElementTree

class Dataspider:

    def __init__(self):
        self._result = list()
        self._url = "www.presta-test.com"
        self._key = "5SIWF2EECP25TZLELM30RGUT8FBBHRD8"

    def get_result(self):
        self._result = self.webservicesPrestapyt()
        return self._result

    def soapconection(self):
        client = SoapClient(
            location = self._url,
            action = self._url, # SOAPAction
            namespace = self._url,
            soap_ns='soap',
            #trace = False,
            ns = False,
            exceptions=True
        )
        # Set WSSE security credentials
        client['wsse:Security'] = {
               'wsse:UsernameToken': {
                    'wsse:Username': self._key,
                    }
                }

        headers = SimpleXMLElement("<products/>")
        response = client.call("products")
        print response

    def webservicesubs(self):
        client = Client(self._url)
        print client

    def webservicesPrestapyt(self):
        prestashop = PrestaShopWebService(self._url, self._key) # messages will be as xml # or
        prestashopdic = PrestaShopWebServiceDict(self._url, self._key) # messages will be as dict
        #prestashop.debug  = True
        #wer = prestashop.get('')
        print prestashopdic.search('products')

    def main(self):
        #self.soapconection()
        #self.webservicesubs()
        self.webservicesPrestapyt()

if __name__ == "__main__":
    spider = Dataspider()
    spider.main()
