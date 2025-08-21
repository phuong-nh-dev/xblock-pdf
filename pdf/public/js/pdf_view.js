/* Javascript for PdfBlock. */
function PdfBlock(runtime, element) {
    var iframe = $('iframe', element);
    var xblock_wrapper = $('.pdf-xblock-wrapper', element);
    var display_name = xblock_wrapper.attr('data-display-name');
    var pdf_url = xblock_wrapper.attr('data-url');

    if(iframe.length > 0){
        iframe.attr('title', display_name);
    }

    function SignalPdfLoaded(ev, presented_within){
        var document_url = $(ev.target).attr('src');
        $.ajax({
            type: "POST",
            url: runtime.handlerUrl(element, 'publish_event'),
            data: JSON.stringify({
                url: document_url,
                displayed_in: presented_within,
                event_type: 'edx.pdf.displayed'
            }),
            success: function(){
                $('.load_event_complete', element).val("I've published the event that indicates that the load has completed");
            }
        });
    }

    function pdfDownloadEvent() {
        $.ajax({
            type: "POST",
            url: runtime.handlerUrl(element, 'on_download'),
            data: JSON.stringify({
                url: pdf_url
            }),
            success: function(){
                console.log('PDF download event tracked');
            }
        });
    }

    iframe.load(function(e){SignalPdfLoaded(e, 'iframe');});

    // Make pdfDownloadEvent globally accessible
    window.pdfDownloadEvent = pdfDownloadEvent;
}