$(document).ready(function() { 
    var options = { 
        target:   '#output',   // target element(s) to be updated with server response 
        beforeSubmit:  beforeSubmit,  // pre-submit callback 
        success:       afterSuccess,  // post-submit callback 
        uploadProgress: OnProgress, //upload progress callback 
        resetForm: true        // reset the form after successful submit 
    }; 
            
     $('#MyUploadForm').submit(function() { 
        $(this).ajaxSubmit(options);  			
        return false; 
    }); 
    });
    