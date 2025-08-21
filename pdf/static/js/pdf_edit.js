/* Javascript for pdfXBlock - Updated for modern compatibility */
function pdfXBlockInitEdit(runtime, element) {
    'use strict';
    
    // Cancel button handler
    $(element).find('.action-cancel').on('click', function (event) {
        event.preventDefault();
        runtime.notify('cancel', {});
    });

    // Save button handler
    $(element).find('.action-save').on('click', function (event) {
        event.preventDefault();
        
        var data = {
            'display_name': $('#pdf_edit_display_name').val().trim(),
            'url': $('#pdf_edit_url').val().trim(),
            'allow_download': $('#pdf_edit_allow_download').val(),
            'source_text': $('#pdf_edit_source_text').val().trim(),
            'source_url': $('#pdf_edit_source_url').val().trim()
        };

        // Validate required fields
        if (!data.display_name) {
            runtime.notify('error', { msg: 'Display name is required' });
            return;
        }
        
        if (!data.url) {
            runtime.notify('error', { msg: 'PDF URL is required' });
            return;
        }

        // Validate URL format
        try {
            new URL(data.url);
        } catch (e) {
            runtime.notify('error', { msg: 'Please enter a valid PDF URL' });
            return;
        }

        runtime.notify('save', { state: 'start' });

        var handlerUrl = runtime.handlerUrl(element, 'save_pdf');
        $.ajax({
            type: 'POST',
            url: handlerUrl,
            data: JSON.stringify(data),
            contentType: 'application/json',
            dataType: 'json'
        })
        .done(function (response) {
            if (response.result === 'success') {
                runtime.notify('save', { state: 'end' });
            } else {
                runtime.notify('error', { 
                    msg: response.message || 'An error occurred while saving' 
                });
            }
        })
        .fail(function (xhr, status, error) {
            runtime.notify('error', { 
                msg: 'Failed to save: ' + (error || 'Unknown error')
            });
        });
    });
}
