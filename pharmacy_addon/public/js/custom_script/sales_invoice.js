frappe.ui.form.on('Sales Invoice', 'refresh', function() {
  frappe.ui.form.on('Sales Invoice Item', {
    item_code: async function(frm, cdt, cdn) {
      const { message = {} } = await frappe.db.get_value(
        'Pharmacy Settings',
        null,
        'default_discount'
      );
      frappe.model.set_value(
        cdt,
        cdn,
        'discount_percentage',
        message['default_discount']
      );
    },
    batch_no: async function(frm, cdt, cdn) {
      const item = locals[cdt][cdn];
      let mrp;
      if (item['batch_no']) {
        const { message = {} } = await frappe.db.get_value(
          'Batch',
          item['batch_no'],
          'mrp'
        );
        mrp = message['mrp'];
      } else {
        const { message = {} } = await frappe.db.get_value(
          'Item Price',
          {
            price_list: frm.doc['selling_price_list'],
            item_code: item['item_code'],
          },
          'price_list_rate'
        );
        mrp = message['price_list_rate'];
      }
      frappe.model.set_value(cdt, cdn, 'price_list_rate', mrp);
    },
  });
});
