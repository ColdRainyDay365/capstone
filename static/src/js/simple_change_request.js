odoo.define('simple_change_request.ui', function (require) {
    "use strict";

    var FormController = require('web.FormController');

    FormController.include({
        _renderView: function () {
            var self = this;
            return this._super.apply(this, arguments).then(function () {
                // Collapsible Effort table
                self.$('.o_collapsible').each(function () {
                    var $group = $(this);
                    if ($group.prev('.o_group_toggle').length === 0) {
                        var header = $('<div class="o_group_toggle">Show Effort Breakdown</div>');
                        header.css({
                            'cursor':'pointer',
                            'font-weight':'bold',
                            'margin':'5px 0',
                            'color':'#333'
                        });
                        $group.before(header);
                        $group.hide();
                        header.on('click', function () {
                            $group.toggle();
                            var isVisible = $group.is(':visible');
                            header.text(isVisible ? 'Hide Effort Breakdown' : 'Show Effort Breakdown');
                        });
                    }
                });
            });
        },
    });

    // Sticky footer buttons
    $(document).ready(function () {
        var footer = $('.o_form_sheet .o_form_footer');
        if (footer.length) {
            footer.css({
                'position': 'sticky',
                'bottom': '0',
                'background': '#fff',
                'padding-top': '5px',
                'padding-bottom': '5px',
                'z-index': '100'
            });
        }
    });
});
