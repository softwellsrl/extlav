#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('codice')
        r.fieldcell('descrizione')
        r.fieldcell('tipo')
        r.fieldcell('tema')
        r.fieldcell('stagione')
        r.fieldcell('colore')

    def th_order(self):
        return 'codice'

    def th_query(self):
        return dict(column='codice', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('codice')
        fb.field('descrizione')
        fb.field('tipo')
        fb.field('tema')
        fb.field('stagione')
        fb.field('colore')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
