#!/usr/bin/env python
# encoding: utf-8
from gnr.app.gnrdbo import GnrDboTable, GnrDboPackage
from datetime import date

class Package(GnrDboPackage):
    def config_attributes(self):
        return dict(comment='lav package',sqlschema='lav',sqlprefix=True,
                    name_short='Lav', name_long='Lavorazioni', name_full='Lav')
                    
    def config_db(self, pkg):
        pass
        
class Table(GnrDboTable):
    
    def insertIfMissing(self,field=None,field_value=None,**kwargs):
        with self.recordToUpdate(**{field:str(field_value)},insertMissing=True) as rec:
            newrecord = not rec['__ins_ts']
            rec.update(kwargs)
            if newrecord:
                self.onNewRecord(rec)
        return rec

    def onNewRecord(self,record):
        pass

    def normalizzaData(self,data_testuale):
        """
        C50325-->datetime.day(2025,
        """
        if not data_testuale:
            return
        giorno = int(data_testuale[-2:])
        mese = int(data_testuale[-4:-2])
        anno = int(data_testuale[1]) + 2020
        return date(anno,mese,giorno)
