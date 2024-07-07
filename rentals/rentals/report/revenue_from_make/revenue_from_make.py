# Copyright (c) 2024, BWH and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):

	# print("---"*20)
	# print(filters)

	# To debug in frontend
	frappe.errprint(filters)
	columns = [{
		"fieldname": "make",
		"label": "Make",
		"fieldType": "Data"
	}, {
		"fieldname": "total_revenue",
		"label": "Total Revenue",
		"fieldType": "Currency",
		"options": "INR"
	}]
	data = frappe.get_all(
		"Ride Booking", 
		fields=["SUM(total_amount) AS total_revenue", "vehicle.make"], 
		filters={"docstatus": 1}, 
		group_by="make"
	)

	chart =  {
		"data": {
		"labels": [x.make for x in data],
		"datasets": [{"values": [x.total_revenue for x in data]}],
	},
		"type": "pie",
	}
	return columns, data, "Here is the summary", chart, 


















# bench --site testsite console --autoreload
# Apps in this namespace:
# frappe, rentals

# In [1]: frappe.get_all("Ride Booking", fields=["total_amount", "vehicle"], filters={"docstatus": 1})
# Out[1]: 
# [{'total_amount': 1080.0, 'vehicle': '3'},
#  {'total_amount': 900.0, 'vehicle': '3'},
#  {'total_amount': 875.0, 'vehicle': '2'},
#  {'total_amount': 220.0, 'vehicle': '3'}]

# In [2]: frappe.get_all("Ride Booking", fields=["total_amount", "vehicle.make"], filters={"docstatus": 1})
# Out[2]: 
# [{'total_amount': 1080.0, 'make': 'Audi'},
#  {'total_amount': 900.0, 'make': 'Audi'},
#  {'total_amount': 875.0, 'make': 'BMW'},
#  {'total_amount': 220.0, 'make': 'Audi'}]

# In [3]: frappe.get_all("Ride Booking", fields=["SUM(total_amount)", "vehicle.make", "COUNT(*)"], filters={"docstatus": 1}, group_by="make")
# Out[3]: 
# [{'SUM(total_amount)': 875.0, 'make': 'BMW', 'COUNT(*)': 1},
#  {'SUM(total_amount)': 2200.0, 'make': 'Audi', 'COUNT(*)': 3}]

# In [4]: frappe.get_all("Ride Booking", fields=["SUM(total_amount) AS total_revenue", "vehicle.make"], filters={"docstatus": 1}, group_by="make")
# Out[4]: 
# [{'total_revenue': 875.0, 'make': 'BMW'},
#  {'total_revenue': 2200.0, 'make': 'Audi'}]