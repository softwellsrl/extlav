# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl=pkg.table('fasonista_sede', pkey='id', name_long='Fasonista sede', 
                        name_plural='Fasonista sedi',caption_field='codice')
        self.sysFields(tbl,counter='fasonista_id')
        tbl.column('fasonista_id',size='22', group='_', name_long='Fasonista'
                    ).relation('fasonista.id', relation_name='sedi', 
                    mode='foreignkey', onDelete='cascade')    
        tbl.column('codice', size=':5', name_long='Codice')
        tbl.column('ragione_sociale', name_long='Ragione sociale')  
        