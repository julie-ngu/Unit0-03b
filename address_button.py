# Created by: Julie Nguyen
# Created on: Sept 2017
# Created for: ICS3U
# Daily Assignment - Unit0-03
# This program is a personal address program, but as a GUI with buttons

import ui

def show_address_touch_up_inside(sender):
    #print ('Julie Nguyen '+'Ottawa '+'Canada')
    view['name_label'].text = ("Julie Nguyen")
    view['city_label'].text = ("Ottawa")
    view['country_label'].text = ("Canada")

view = ui.load_view()
view.present('sheet')
