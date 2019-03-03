$(document).ready(function(){
  $(".menu-icon").on("click",function(){
    $("nav ul").toggleClass("showing");
  });

  $(window).on("load", function() {
    preloaderFadeOutTime = 500;
    function hidePreloader() {
      var preloader = $('#wrapper');
      preloader.fadeOut(preloaderFadeOutTime);
      }
      hidePreloader();
  });

});

$(window).on("scroll",function(){
  if($(window).scrollTop()){
    $('nav').addClass('black');
  }
  else{
    $('nav').removeClass('black');
  }
});
