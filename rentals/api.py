import frappe

# Decorator to allow the user to access this api
# allow_guest=True is used to access by the guests
@frappe.whitelist(allow_guest=True)
def get_emoji():
    return "This Is From API"

def send_payment_remainders():
    pass

# def get_query_conditions_for_vehicle(user):
#     return "name = 2"