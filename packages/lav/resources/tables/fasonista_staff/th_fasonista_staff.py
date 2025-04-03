#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method
class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('_row_count')
        r.fieldcell('fasonista_id')
        r.fieldcell('nome')
        r.fieldcell('cognome')
        r.fieldcell('email')

    def th_order(self):
        return '_row_count'

    def th_query(self):
        return dict(column='_row_count', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2)
        fb.field('_row_count')
        fb.field('fasonista_id')
        fb.field('nome')
        fb.field('cognome')
        fb.field('email')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')


class ViewFromFasonista(BaseComponent):
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('_row_count',counter=True)
        r.fieldcell('nome')
        r.fieldcell('cognome')
        r.fieldcell('email')
        r.fieldcell('user_group')


class FormFromFasonista(BaseComponent):
    def th_form(self, form):
        pane = form.record
        fb = pane.formlet(cols=2)
        fb.field('nome',validate_notnull=True)
        fb.field('cognome',validate_notnull=True)
        fb.field('email',colspan=2,validate_notnull=True,unmodifable=True)
        fb.field('user_group',condition='$code!=:wsai',
                    condition_wsai='WSAI',hasDownArrow=True)
        btn = fb.lightButton('Crea utente',
                hidden='^.@user.id',font_weight='bold',
                text_decoration='underline')
        btn.dataController(
            """
            var that = this;
            if(this.form.canBeSaved()){
                this.form.save({onReload:function(){
                    that.fireEvent('#FORM.crea_utente',true);
                }})
            }else{
                FIRE #FORM.crea_utente;
            }
            
            """
        )
        pane.dataRpc(self.creaUtenteStaff,staff_id='=#FORM.pkey',
        _fired='^#FORM.crea_utente',_lockScreen=True,
        _onResult="this.form.reload();")


    @public_method
    def creaUtenteStaff(self,staff_id=None):
        self.db.table('lav.fasonista_staff').creaUtente(
            staff_id=staff_id
        )
        self.db.commit()


    def th_options(self):
        return dict(dialog_height='230px', dialog_width='400px')

