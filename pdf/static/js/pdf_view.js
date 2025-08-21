/* Javascript for pdfXBlock - Updated for modern compatibility */
function pdfXBlockInitView(runtime, element) {
    'use strict';
    
    // Ensure element is jQuery object for consistency
    if (element.innerHTML) {
        element = $(element);
    }

    $(function () {
        element.find('.pdf-download-button').on('click', function (event) {
            // Prevent default action to handle tracking
            event.preventDefault();
            
            var handlerUrl = runtime.handlerUrl(element, 'on_download');
            var downloadUrl = $(this).find('a').attr('href');
            
            // Send tracking event
            $.post(handlerUrl, JSON.stringify({}))
                .done(function (response) {
                    console.log('PDF download tracked successfully');
                })
                .fail(function (xhr, status, error) {
                    console.warn('Failed to track PDF download:', error);
                })
                .always(function () {
                    // Proceed with actual download
                    if (downloadUrl) {
                        window.open(downloadUrl, '_blank');
                    }
                });
        });
    });
}
