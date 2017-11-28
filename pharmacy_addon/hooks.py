# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "pharmacy_addon"
app_title = "Pharmacy Addon"
app_publisher = "Libermatic"
app_description = "Extensions for pharmacy management"
app_icon = "fa fa-medkit"
app_color = "grey"
app_email = "info@libermatic.com"
app_license = "MIT"
fixtures = [{
        'doctype': 'Custom Field',
        'filters': { 'dt': 'Batch', 'fieldname': 'mrp' }
    }, {
        'doctype': 'Custom Script',
        'filters': { 'dt': 'Sales Invoice' }
    }, {
        'doctype': 'Property Setter',
        'filters': [
                { 'doc_type': 'Sales Invoice Item' },
                [
                    'field_name',
                    'in',
                    (
                        'item_code',
                        'qty',
                        'uom',
                        'price_list_rate',
                        'discount_percentage',
                        'rate',
                        'amount',
                        'batch_no',
                        'warehouse'
                    )]
            ]
    }, {
        'doctype': 'Property Setter',
        'filters': [
                { 'doc_type': 'Purchase Invoice Item' },
                [
                    'field_name',
                    'in',
                    (
                        'item_code',
                        'qty',
                        'uom',
                        'price_list_rate',
                        'discount_percentage',
                        'rate',
                        'amount',
                        'batch_no'
                    )]
            ]
    }]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/pharmacy_addon/css/pharmacy_addon.css"
# app_include_js = "/assets/pharmacy_addon/js/pharmacy_addon.js"

# include js, css files in header of web template
# web_include_css = "/assets/pharmacy_addon/css/pharmacy_addon.css"
# web_include_js = "/assets/pharmacy_addon/js/pharmacy_addon.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "pharmacy_addon.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "pharmacy_addon.install.before_install"
# after_install = "pharmacy_addon.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "pharmacy_addon.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"pharmacy_addon.tasks.all"
# 	],
# 	"daily": [
# 		"pharmacy_addon.tasks.daily"
# 	],
# 	"hourly": [
# 		"pharmacy_addon.tasks.hourly"
# 	],
# 	"weekly": [
# 		"pharmacy_addon.tasks.weekly"
# 	]
# 	"monthly": [
# 		"pharmacy_addon.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "pharmacy_addon.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "pharmacy_addon.event.get_events"
# }
