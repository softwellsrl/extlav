# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('articolo_stagione', pkey='codice', name_long='Stagione', name_plural='Stagioni',caption_field='descrizione',lookup=True)
        self.sysFields(tbl,counter=True,id=False)
        tbl.column('codice', size=':3', name_long='Codice')
        tbl.column('descrizione', name_long='Descrizione')
        