/* Javascript for PdfEditBlock. */
function PdfEditBlock(runtime, element) {
  $(element)
    .find(".cancel-button")
    .on("click", function (e) {
      e.preventDefault();
      runtime.notify("cancel", {});
    });

  $(element)
    .find(".save-button")
    .on("click", function (e) {
      e.preventDefault();
      var handlerUrl = runtime.handlerUrl(element, "studio_submit");
      var data = {
        display_name: $(element).find("input[id=edit_display_name]").val(),
        url: $(element).find("input[id=edit_url]").val(),
      };

      runtime.notify("save", { state: "start" });

      $.post(handlerUrl, JSON.stringify(data))
        .done(function (response) {
          if (response.result === "success") {
            runtime.notify("save", { state: "end" });
          } else {
            runtime.notify("error", { msg: response.message });
          }
        })
        .fail(function () {
          runtime.notify("error", { msg: "Unable to update settings" });
        });
    });

  $(element)
    .find(".setting-clear")
    .on("click", function (e) {
      e.preventDefault();
      var $input = $(this).siblings("input");
      var default_value = $input.data("default-value");
      $input.val(default_value);
    });
}
