#!/usr/bin/python3
# -*- coding: utf-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('codice')
        r.fieldcell('nome')

    def th_order(self):
        return 'codice'

    def th_query(self):
        return dict(column='id', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        fb = bc.contentPane(region='top',datapath='.record').formlet(cols=2, border_spacing='4px')
        fb.field('codice' )
        fb.field('nome' )
        tc = bc.tabContainer(region='center',margin='2px')
        tc.contentPane(title='Staff').dialogTableHandler(
            relation='@staff',
            viewResource='ViewFromFasonista',
            formResource='FormFromFasonista'
        )
        tc.contentPane(title='Commesse').dialogTableHandler(relation='@commesse')

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' )


class FormProfilo(BaseComponent):
    def th_form(self, form):

        bc = form.center.borderContainer()
        fb = bc.contentPane(region='top',datapath='.record').formlet(cols=2, border_spacing='4px')
        fb.field('codice' ,readOnly=True)
        fb.field('nome'  ,readOnly=True)
        tc = bc.tabContainer(region='center',margin='2px')
        tc.contentPane(title='Staff').dialogTableHandler(
            relation='@staff',
            viewResource='ViewFromFasonista',
            formResource='FormFromFasonista'
        )

    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px' ,showtoolbar=False)
