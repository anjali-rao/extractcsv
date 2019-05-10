
;( function(global){

global.CSRF_TOKEN = function(name) {
                        var cookieValue = null;
                        if (document.cookie && document.cookie != '') {
                            var cookies = document.cookie.split(';');
                            for (var i = 0; i < cookies.length; i++) {
                                var cookie = $.trim(cookies[i]);
                                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                                    break;
                                }
                            }
                        }
                        return cookieValue;
                    };

global.postRequest = function(url, params){
                       return  $.ajax({
                            url: url,
                            type: "POST",
                            data: params,
                            headers: {
                                "X-CSRFToken": global.CSRF_TOKEN("csrftoken")
                            },
                            dataType: "json",
                        });
                    }

global.displayError = function(selector, message) {

                        var errorDisp = $(document).find(selector);
                        errorDisp.addClass("alert alert-danger");
                        errorDisp.text(message);

                        $(selector).fadeOut(
                            2000,
                            function(){
                                $(this).remove();
                            }
                        );

                    };
})(window.csvdata = window.csvdata || {});
