 $(document).on('click', '.pagination a', function(event){
      event.preventDefault();
      $('html, body').animate({
        scrollTop: 0
      }, 'fast');
      $('.loader').show(); // affiche l'image de chargement
      $.get($(this).attr('href'), function(data){
        $('.loader').hide(); // cache l'image de chargement
        $('#stock-items').html(data);
        history.replaceState({}, '', $(this).attr('href')); // met à jour l'URL de la page
            location.reload()
      }.bind(this));
    });


    $(document).on('click', '.go-button', function(event){
      event.preventDefault();
      $('html, body').animate({
        scrollTop: 0
      }, 'fast');
      var pageNumber = $('.page-input').val();
      var url = '?page=' + pageNumber;
      $('.loader').show(); // affiche l'image de chargement
      $.get(url, function(data){
        $('.loader').hide(); // cache l'image de chargement
        //$('#stock-items').html(data);
        history.replaceState({}, '', url); // met à jour l'URL de la page
      });
    });

