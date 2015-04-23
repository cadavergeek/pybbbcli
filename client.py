from pybbbcli import Pybbbcli

bike_values = {
    "make": "GT",
    "model": "XCR-2000",
    "year": 2000
    }



# Sin valores iniciales
#bbb = Pybbbcli()
# traemos las marcas
#bbb.searchBrands()
#bbb.showBrands()
#bbb.selectBrand()

# traemos los modelos
#bbb.searchModels()
#bbb.showModels()
#bbb.selectModel()

#bbb.searchYears()
#bbb.showYears()
#bbb.selectYear()

#print bbb.values
#bbb.searchBikePrice()

c = Pybbbcli.from_bike_info(**bike_values)
c.searchBikePrice()