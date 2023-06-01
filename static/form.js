$(document).ready(function(){
    $('.btn-get-started').click(function(){
      const message = $('[name=message]').val();
        if(message == "")
        {

        }
        else
        {
          $.ajax({
            
              url   : '/create_file',
             type : 'POST',
             data   : {input : $('#input').val()},
            dataType: 'text',
            success : function(data){
              alert(data);
             }
             
          });
        }


    });
    
  });