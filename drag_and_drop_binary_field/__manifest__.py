# Copyright 2023 Nicolae Postica <nicolae.postica2@gmail.com>
{
    "name": "Drag And Drop Binary Field Widget",
    "version": "16.0.1.0.0",
    "summary": """
        The Drag and Drop Binary Field Widget for Odoo
        is a custom widget that enhances the user experience when
        dealing with binary fields.
    """,
    "license": "AGPL-3",
    "price": 0,
    "currency": "EUR",
    "author": "Nicolae Postica,Arkana Solusi Digital (ASD)",
    "support": "nicolae.postica2@gmail.com",
    "website": "https://github.com/ArkanaDigital/medika-medivac",
    "images": [
        "static/description/main.png",
    ],
    "category": "Tools",
    "depends": ["base_setup"],
    "data": [],
    "assets": {
        "web.assets_backend": [
            "drag_and_drop_binary_field/static/src/js/field_binary.js",
            "drag_and_drop_binary_field/static/src/js/field_image.js",
            "drag_and_drop_binary_field/static/src/js/field_man2many_binary.js",
        ],
    },
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "auto_install": False,
    "installable": True,
}
