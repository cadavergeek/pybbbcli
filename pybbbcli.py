import requests
from bs4 import BeautifulSoup


class Pybbbcli:

    @classmethod
    def from_bike_info(cls, **kwargs):
        make = kwargs["make"]
        model = kwargs["model"]
        year = kwargs["year"]
        return cls(make, model, year)

    def __init__(self, make=None, model=None, year=None):
        self.baseUrl = "http://www.bicyclebluebook.com/"
        self.searchUrl = "SearchListing.aspx"
        self.brands = {}
        self.years = {}
        self.models = {}
        self.HTMLIDFilters = {
            "make": "contentBody_ddlFilterMake",
            "model": "contentBody_ddlFilterModel",
            "year": "contentBody_ddlFilterYear",
            "final": "search-result"
        }

        self.values = {
            "make": make,
            "model": model,
            "year": year
        }
        
    def _parseSelectOption(self, soupObj):
        #options = soupObj.find_all("option")
        values_dict = {}    
        for o in soupObj:
            values_dict[o.text] = o["value"]
        return values_dict
    
    def _parseTableInfo(self, soupObj):
        print soupObj

    def _parseHtmlResponse(self, htmlResp, htmlID, controlType="select"):
        """Private method used to extract information from request done website
        :param htmlResp: html response
        :param htmlID: html response ID to get info from
        :returns: dict with obtained values
        """
        soup = BeautifulSoup(htmlResp)
        getSelectControl = soup.find(controlType, {"id": htmlID})
        
        if controlType == "select":
            return self._parseSelectOption(getSelectControl.find_all("option"))
        elif controlType == "table":
            self._parseTableInfo(getSelectControl.find_all("td"))
            
    def _search(self, searchType, queryStr, extra=None):
        """This search is used for information searching on site 
        using requests module
        :param searchType: str representing the type of search 
        :returns: dict obj with values 
        """
        r = requests.get("".join([self.baseUrl, self.searchUrl, queryStr]))
        if not extra:
            return self._parseHtmlResponse(r.text, self.HTMLIDFilters[searchType])
        else:
            return self._parseHtmlResponse(r.text, self.HTMLIDFilters[searchType], extra)


    def searchBrands(self):
        self.brands = self._search("make", "")
        
    def searchModels(self):
        if self.values["make"]:
            queryStr="?make={0}".format(self.values["make"])
            self.models = self._search("model", queryStr)
        else:
            print "Select a brand first"

    def searchYears(self):
        if self.values["make"] and self.values["model"]:
            queryStr="?make={0}&model={1}".format(self.values["make"],self.values["model"])
            self.years = self._search("year", queryStr)
        else:
            print "Select a model first"
    
    def searchBikePrice(self):
        queryStr = "?make={0}&model={1}&year={2}".format(
            self.values["make"],
            self.values["model"],
            self.values["year"]
        )
        self._search("final", queryStr, "table")

    def _showOptions(self, optionsDict):
        """Print options list"""
        if optionsDict:
            for val in optionsDict.keys():
                print val
        else:
            print "Option list is empty"

    def showBrands(self):
        """Method used to print brands available to user"""
        self._showOptions(self.brands)

    def showModels(self):
        """Method used to print brands available to user"""
        self._showOptions(self.models)
        
    def showYears(self):
        """Method used to print available years to user"""
        self._showOptions(self.years)
            
    def _select(self, selectOption, optionsObj):
        """This method receive the user input for the choosen band"""
        valid = False
        
        while not valid:
            value = raw_input("Type the number of {0}: ".format(selectOption))
            try:
                self.values[selectOption] = optionsObj[value]
                valid = True
            except KeyError:
                print "Selection was invalid. Please enter correct value"
        return value
    
    def selectBrand(self):
        self.brand = self._select("make", self.brands)
        
    def selectModel(self):
        self.model = self._select("model", self.models)
        
    def selectYear(self):
        self.year = self._select("year", self.years)