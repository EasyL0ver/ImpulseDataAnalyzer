import ormprovider as orm
import datamodels as dm
import dataprovider as dp


ormprov = orm.DataProvider();
dataprov = dp.DataProvider(ormprov.getActiveSession());
dataprov.datasources.append(r"D:\moje\testdata")
dataprov.loaddata()
