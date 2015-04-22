from pybbbcli import Pybbbcli

bbb = Pybbbcli()
print bbb       
allbrands = bbb.search()
bbb.showBrands()
bbb.select()

models = bbb.search("model")
bbb.showModels()
print bbb.select("model")