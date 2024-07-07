// Copyright (c) 2024, BWH and contributors
// For license information, please see license.txt

frappe.ui.form.on("Vehicle", {
	refresh(frm) {

	},

    get_summary(frm) {
        if (!frm.get_field("summary").$wrapper.find(".summary-content").length) {
            frm.get_field("summary").$wrapper.append('<div class="summary-content"><h2>Here\'s your summary</h2></div>');
        }
    }
});
