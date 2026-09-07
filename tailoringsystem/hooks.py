app_name = "tailoringsystem"
app_title = "Tailoringsystem"
app_publisher = "Anas Al-Dharei"
app_description = "Tailoring Management System"
app_email = "anas202255@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "tailoringsystem",
# 		"logo": "/assets/tailoringsystem/logo.png",
# 		"title": "Tailoringsystem",
# 		"route": "/tailoringsystem",
# 		"has_permission": "tailoringsystem.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/tailoringsystem/css/tailoringsystem.css"
# app_include_js = "/assets/tailoringsystem/js/tailoringsystem.js"

# include js, css files in header of web template
# web_include_css = "/assets/tailoringsystem/css/tailoringsystem.css"
# web_include_js = "/assets/tailoringsystem/js/tailoringsystem.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "tailoringsystem/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "tailoringsystem/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "tailoringsystem.utils.jinja_methods",
# 	"filters": "tailoringsystem.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "tailoringsystem.install.before_install"
# after_install = "tailoringsystem.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "tailoringsystem.uninstall.before_uninstall"
# after_uninstall = "tailoringsystem.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "tailoringsystem.utils.before_app_install"
# after_app_install = "tailoringsystem.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "tailoringsystem.utils.before_app_uninstall"
# after_app_uninstall = "tailoringsystem.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "tailoringsystem.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "tailoringsystem.notifications.get_notification_config"

# Awesome Bar
# -----------
# Extra search results: list of dicts with label, description, route, index.
# route: ["List", "ToDo"], "/desk/docs/some/page", or "https://example.com"
# awesomebar_search = ["tailoringsystem.search.awesomebar_results"]

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
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"tailoringsystem.tasks.all"
# 	],
# 	"daily": [
# 		"tailoringsystem.tasks.daily"
# 	],
# 	"hourly": [
# 		"tailoringsystem.tasks.hourly"
# 	],
# 	"weekly": [
# 		"tailoringsystem.tasks.weekly"
# 	],
# 	"monthly": [
# 		"tailoringsystem.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "tailoringsystem.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "tailoringsystem.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "tailoringsystem.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "tailoringsystem.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["tailoringsystem.utils.before_request"]
# after_request = ["tailoringsystem.utils.after_request"]

# Job Events
# ----------
# before_job = ["tailoringsystem.utils.before_job"]
# after_job = ["tailoringsystem.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"tailoringsystem.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

