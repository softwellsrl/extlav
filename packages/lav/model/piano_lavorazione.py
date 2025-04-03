# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('piano_lavorazione',pkey='id',
                        name_long='Piano lavorazione',
                        name_plural='Piani lavorazione',caption_field='id')
        self.sysFields(tbl)
        tbl.column('protocollo',size=':10',name_long='protocollo')
        tbl.column('data_inizio_sett', dtype='D', 
                    name_long='Data inizio sett.', 
                    name_short='Inizio sett.')


    def importBollettine(self,reader,piano_lavorazione_id=None):
        for riga in reader():
            self.db.table('lav.piano_lavorazione_riga').importaRiga(
                riga=riga,
                piano_lavorazione_id=piano_lavorazione_id
            )

