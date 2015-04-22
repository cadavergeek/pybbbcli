import requests
from bs4 import BeautifulSoup


class Pybbbcli:

    def __init__(self, make=None, model=None, year=None):
        self.baseUrl = "http://www.bicyclebluebook.com/"
        self.searchUrl = "SearchListing.aspx"
        self.make = {}
        self.year = {}
        self.model = {}
        self.HTMLIDFilters = {
            "make": "contentBody_ddlFilterMake",
            "model": "contentBody_ddlFilterModel",
            "year": "contentBody_ddlFilterYear"
        }

        self.values = {
            "make": None,
            "model": None,
            "year": None
        }
        
        self.search()
    
    def _parseHtmlResponse(self, htmlResp, htmlID):
        """Private method used to extract information from request done website
        :param htmlResp: html response
        :param htmlID: html response ID to get info from
        :returns: dict with obtained values
        """
        values_dict = {}
        soup = BeautifulSoup(htmlResp)
        getSelectControl = soup.find("select", {"id": htmlID})
        options = getSelectControl.find_all("option")
        for o in options:
            values_dict[o.text] = o["value"]
        return values_dict
            
    def search(self, searchType="make", *args, **kwargs):
        """This search is used for information searching on site 
        using requests module
        :param brand: str represeting bicycle brand 
        :param model: str represeting bicycle model 
        :param year: str represeting bicycle year
        :returns: dict obj with values 
        """
        
        if searchType == "model"
            extraparams = "?make="+id+"
        elif searchtype == "year"
            extraparams = "?make+id+&model+id
        elif:
            extraparams =""
        
        
        
        if not self.values["make"]:
            r = requests.get("".join([self.baseUrl, self.searchUrl, extraparams]))
        else:
            temp_url = "".join([self.baseUrl, self.searchUrl, "?make={0}".format(self.values["make"])])
            print temp_url
            r = requests.get(temp_url)
        parsed = self._parseHtmlResponse(r.text, self.HTMLIDFilters[searchType])
        if searchType == "make":
            self.brands = parsed
        elif searchType == "model":
            self.model = parsed
    
    def showBrands(self):
        """Method used to print brands available to user"""
        if self.brands:
            for key in self.brands.keys():
                print key
        else:
            print "No brands available. :("
            
    def showModels(self):
        """Method used to print brands available to user"""
        if self.model:
            for key in self.model.keys():
                print key
        else:
            print "No models available. :("
            
    def select(self, select="make"):
        """This method receive the user input for the choosen band"""
        valid = False
        
        while not valid:
            value = raw_input("Type the number of {0}: ".format(select))
            try:
                self.values[select] = value
                valid = True
            except KeyError:
                print "Selection was invalid. Please enter correct value"