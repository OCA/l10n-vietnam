import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo11-addons-oca-l10n-vietnam",
    description="Meta package for oca-l10n-vietnam Odoo addons",
    version=version,
    install_requires=[
        'odoo11-addon-currency_rate_update_VN_VCB',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
