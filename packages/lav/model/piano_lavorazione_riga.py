# encoding: utf-8


class Table(object):
    def config_db(self, pkg):
        tbl =  pkg.table('piano_lavorazione_riga',pkey='id',name_long='Riga piano',name_plural='Righe piano',caption_field='id')
        self.sysFields(tbl)
        tbl.column('piano_lavorazione_id',size='22',name_long='Piano lavorazione').relation('piano_lavorazione.id',
                    relation_name='righe', mode='foreignkey',onDelete='cascade')
        tbl.column('commessa_id',size='22',name_long='Commessa').relation('commessa.id',relation_name='righe_pianolavorazione')
        tbl.column('inizio_assemblaggio', dtype='D', name_long='Inizio assemblaggio')
        tbl.column('priorita', dtype='L', name_long='Priorità')
        tbl.column('inizio_cucitura', dtype='D', name_long='Inizio cucitura')

        tbl.column('inizio_confezionamento', dtype='D', name_long='Inizio confezionamento')

        tbl.column('data_evasione', dtype='D', name_long='Data evasione')
        tbl.column('data_spedizione', dtype='D', name_long='Data spedizione')

        tbl.column('quantita_da_produrre', dtype='L', name_long='Quantità da produrre')


    def importaRiga(self,riga,piano_lavorazione_id=None):

        """['codice_terzista', 'ragione_sociale', 'codice_destinazione', 'descrizione_destinazione', 
        'numero_bollettina', 'data_bollettina', 'articolo', 
        'descrizione_articolo', 'data_consegna', 'numero_pezzi_bollettina',
         'numero_pezzi_da_produrre', 'priorita', 'flag_evasa', 'cod_tema',
          'descrizione_tema', 'codstagione', 'descrizione_stagione']"""
        self.insert(self.newrecord(
            piano_lavorazione_id=piano_lavorazione_id,
            quantita_da_produrre=riga['numero_pezzi_da_produrre'],
            commessa_id=self.db.table('lav.commessa').insertIfMissing(
                        field='codice_commessa',
                        field_value=riga['numero_bollettina'],
                        riga_importazione=riga,
                        quantita=riga['numero_pezzi_bollettina']
                    )['id']
        ))
    
