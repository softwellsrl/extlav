#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('_row_count')
        r.fieldcell('fasonista_id')
        r.fieldcell('codice')
        r.fieldcell('ragione_sociale')

    def th_order(self):
        return '_row_count'

    def th_query(self):
        return dict(column='_row_count', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.formbuilder(cols=2, border_spacing='4px')
        fb.field('_row_count')
        fb.field('fasonista_id')
        fb.field('codice')
        fb.field('ragione_sociale')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
