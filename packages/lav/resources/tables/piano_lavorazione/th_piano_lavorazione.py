#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
from gnr.core.gnrlist import getReader


class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('protocollo')

    def th_order(self):
        return 'protocollo'

    def th_query(self):
        return dict(column='id', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        fb = bc.contentPane(region='top').formlet(cols=2, 
                                border_spacing='4px',
                                datapath='.record')
        fb.field('data_inizio_sett')
        th = bc.contentPane(region='center'
                        ).plainTableHandler(relation='@righe')
        th.view.bottom.dropUploader(height='118px', width='498px',
                            label="<div style='padding:20px'>Trascina qui il file Excel da importare</div>",
                            uploadPath='page:piano_uploaded.csv',
                            rpc_piano_lavorazione_id='=#FORM.record.id',
                            progressBar=True,
                            rpc__lockScreen=True,
                            onUploadedMethod=self.onUploadedPianoLav,
                            onResult='this.form.reload();')

    @public_method
    def onUploadedPianoLav(self,file_path=None,piano_lavorazione_id=None,**kwargs):
        sn = self.site.storageNode(file_path)
        reader = getReader(sn.internal_path)
        self.db.table('lav.piano_lavorazione').importBollettine(
            reader=reader,
            piano_lavorazione_id=piano_lavorazione_id
        )
        self.db.commit()
        
        

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )
