# encoding: utf-8
class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('articolo_tipo', pkey='codice', 
                            name_long='Tipo articolo', 
                        name_plural='Tipi articoli',
                        caption_field='descrizione',lookup=True)
        self.sysFields(tbl,id=False,counter=True)
        tbl.column('codice', size=':2', name_long='Codice')
        tbl.column('descrizione', name_long='Descrizione')
        

    def sysRecord_MP(self):
        return self.newrecord(
            codice='MP',
            descrizione='Materia prima'
        )

    def sysRecord_PF(self):
        return self.newrecord(
            codice='PF',
            descrizione='Prodotto finito'
        )