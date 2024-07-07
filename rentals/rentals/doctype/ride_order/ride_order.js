// Copyright (c) 2024, BWH and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
    onload(frm){
      console.log("Running Load....")  
    },
    setup(frm){
      console.log('Setup.....')  
    },
	refresh(frm) {
        console.log('refresh.....')
        if(frm.doc.status === "New"){
            frm.add_custom_button("Accept", () => {
                frm.set_value("status", "Accepted")
                // Save the form
                frm.save()
            }, "Actions")

            frm.add_custom_button("Rejected", () => {
                frm.set_value("status", "Rejected")
                // Save the form
                frm.save()
            }, "Actions")
        }
	},
    status(frm){
        console.log("Status Changed....")
    }
});
