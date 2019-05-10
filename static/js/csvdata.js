;(function() {
    var postRequest = window.csvdata.postRequest;

    function getData(){
        var filname = $("#filename").val();
        var fields = $("#fields").val();
        var url = "/get_data?"
        var params = {
            filename: $("#filename").val(),
            fields: $("#fields").val()
        };
		var selector = "#csv_data";
        var request = postRequest(url, params);
         request.done(function(result){
			$(selector).empty()
            if (result.success){
                $(selector).append(result.html);
            } else {
                $(selector).append("<span class='text-muted ml-4'>No data found</span>");
            }
            console.log("done");
         });
    }
    
    $(document).on("click", "#get-data", getData);
})();
