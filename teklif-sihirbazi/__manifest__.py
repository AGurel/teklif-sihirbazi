{
    'name': "Teklif Sihirbazı",
    'version': '1.0',
    'summary': 'Teklifler',
    'depends': ['base'],
    'author': "A.Gurel",
    'category': 'Sales',
    'description': "Bu sihirbazı kullanarak hızlı ve pratik teklifler hazırlayabilirsiniz.",
    'website': "http://www.versusyazilim.com",
    'installable': True,
    'application': True,
    'auto_install': False,
    
    'data': [
    
        'security/ir.model.access.csv',
        
        'views/teklif_views.xml',
        
        'views/teklif_menus.xml'
        
        ]
}