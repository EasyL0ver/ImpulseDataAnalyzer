import ormprovider as orm
import datamodels as dm
import dataprovider as dp
import common


ormprov = orm.DBProvider();
dataprov = dp.DataProvider(ormprov.get_session());
dataprov.sources.append(r"D:\inzynierka\ImpulseDataAnalyzer")
dataprov.load_data()
dataprov.load_data()
dataprov.load_data()
dataprov.populate()



loadtest = dataprov.loaded_data[0]

data = common.binarytonp(loadtest.dat1)
var = 1

