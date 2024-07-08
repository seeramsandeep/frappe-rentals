import frappe

def get_context(context):
    context.my_name = frappe.session.user or "Dear"