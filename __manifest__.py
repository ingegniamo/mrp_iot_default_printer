# -*- coding: utf-8 -*-
{
    'name': "Mrp iot default printer",
    
    'summary': "",
  
    'license': 'OPL-1',

    'author': "STeSI Consulting",

    'category': '',
  
    'version': '18.0.0.1',
  
    'website': "http://www.stesi.consulting",

    # any module necessary for this one to work correctly
    'depends': ['iot','mrp'],
    
    # always loaded
    'data': ['views/mrp_production.xml'],

    'application': False,
}
