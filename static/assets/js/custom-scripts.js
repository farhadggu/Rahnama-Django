(function($) {
  'use strict';

  //===== Delay Anmiation =====// 
  var drop = $('.featured-cap > *');
  $('.featured-cap').each(function () {
    var delay = 0;
    $(this).find(drop).each(function () {
      $(this).css({ transitionDelay: delay + 'ms' });
      delay += 200;
    });
  });

  //===== Header Search =====//
  $('.srch-btn').on('click', function () {
    $('.header-search').addClass('active');
    return false;
  });
  $('.srch-cls-btn').on('click', function () {
    $('.header-search').removeClass('active');
    return false;
  });

  //===== Side Panel =====//
  $(".sidepanel > span").on('click', function () {
    $(".sidepanel").toggleClass("show");
    $(this).toggleClass('spin');
    return false;
  });

  //===== Color Picker =====*/
  $('.color-picker a').on("click", function () {
    $('.color-picker a').removeClass("applied");
    $(this).addClass("applied");
    return false;
  });

  //===== Contact Form Popup =====*/
  $('.contact-btn').on('click', function () {
    $('.contact-form-model-wrap').addClass('active');
    return false;
  });
  $('.model-close').on('click', function () {
    $('.contact-form-model-wrap').removeClass('active');
    return false;
  });

  //===== Responsive Header =====//
  $('.rspn-mnu-btn').on('click', function () {
    $('.rsnp-mnu').addClass('slidein');
    return false;
  });
  $('.rspn-mnu-cls').on('click', function () {
    $('.rsnp-mnu').removeClass('slidein');
    return false;
  });
  $('.rsnp-mnu li.menu-item-has-children > a').on('click', function () {
    $(this).parent().siblings().children('ul').slideUp();
    $(this).parent().siblings().removeClass('active');
    $(this).parent().children('ul').slideToggle();
    $(this).parent().toggleClass('active');
    return false;
  });

  //===== Scrollbar =====//
  if ($('.rsnp-mnu, .contact-form-inner').length > 0) {
    var ps = new PerfectScrollbar('.rsnp-mnu, .contact-form-inner');
  }

  //===== LightBox =====//
  if ($.isFunction($.fn.fancybox)) {
    $('[data-fancybox],[data-fancybox="gallery"]').fancybox({});
  }

  //===== Select =====//
  if ($('select').length > 0) {
    $('select').selectpicker();
  }

  //===== Circliful =====//
  if ($.isFunction($.fn.circliful)) {
    $("#suprt-prg1").circliful({
      animationStep: 5,
      foregroundBorderWidth: 10,
      backgroundBorderWidth: 10,
      backgroundColor: '#2a486c',
      foregroundColor: '#d1ad3c',
      animateInView: true,
      textColor: '#d1ad3c',
      fontColor: '#fff',
      percent: 46,
      text: 'ساخت مساجد',
      textBelow: true,
      textStyle: 'font-size: 18px'
    });

    $("#suprt-prg2").circliful({
      animationStep: 5,
      foregroundBorderWidth: 10,
      backgroundBorderWidth: 10,
      backgroundColor: '#2a486c',
      foregroundColor: '#d1ad3c',
      animateInView: true,
      textColor: '#d1ad3c',
      fontColor: '#fff',
      percent: 56,
      text: 'تدریس ها',
      textBelow: true,
      textStyle: 'font-size: 18px'
    });

    $("#suprt-prg3").circliful({
      animationStep: 5,
      foregroundBorderWidth: 10,
      backgroundBorderWidth: 10,
      backgroundColor: '#2a486c',
      foregroundColor: '#d1ad3c',
      animateInView: true,
      textColor: '#d1ad3c',
      fontColor: '#fff',
      percent: 75,
      text: 'کمک به فقرا',
      textBelow: true,
      textStyle: 'font-size: 18px'
    });

    $("#suprt-prg4").circliful({
      animationStep: 5,
      foregroundBorderWidth: 10,
      backgroundBorderWidth: 10,
      backgroundColor: '#2a486c',
      foregroundColor: '#38ab1e',
      animateInView: true,
      textColor: '#d1ad3c',
      fontColor: '#fff',
      percent: 46,
      text: 'مساجد',
      textBelow: true,
      textStyle: 'font-size: 18px'
    });

    $("#suprt-prg5").circliful({
      animationStep: 5,
      foregroundBorderWidth: 10,
      backgroundBorderWidth: 10,
      backgroundColor: '#2a486c',
      foregroundColor: '#38ab1e',
      animateInView: true,
      textColor: '#d1ad3c',
      fontColor: '#fff',
      percent: 56,
      text: 'تدریس ها',
      textBelow: true,
      textStyle: 'font-size: 18px'
    });

    $("#suprt-prg6").circliful({
      animationStep: 5,
      foregroundBorderWidth: 10,
      backgroundBorderWidth: 10,
      backgroundColor: '#2a486c',
      foregroundColor: '#38ab1e',
      animateInView: true,
      textColor: '#d1ad3c',
      fontColor: '#fff',
      percent: 75,
      text: 'فقرا',
      textBelow: true,
      textStyle: 'font-size: 18px'
    });

    $("#expns-prg1").circliful({
      animationStep: 5,
      foregroundBorderWidth: 12,
      backgroundBorderWidth: 12,
      backgroundColor: '#e1e1e1',
      foregroundColor: '#2d4b6f',
      animateInView: true,
      textColor: '#d1ad3c',
      fontColor: '#a1a1a1',
      percent: 46,
    });

    $("#expns-prg2").circliful({
      animationStep: 5,
      foregroundBorderWidth: 12,
      backgroundBorderWidth: 12,
      backgroundColor: '#e1e1e1',
      foregroundColor: '#2d4b6f',
      animateInView: true,
      textColor: '#d1ad3c',
      fontColor: '#a1a1a1',
      percent: 60,
    });

    $("#expns-prg3").circliful({
      animationStep: 5,
      foregroundBorderWidth: 12,
      backgroundBorderWidth: 12,
      backgroundColor: '#e1e1e1',
      foregroundColor: '#2d4b6f',
      animateInView: true,
      textColor: '#d1ad3c',
      fontColor: '#a1a1a1',
      percent: 50,
    });

    $("#expns-prg4").circliful({
      animationStep: 5,
      foregroundBorderWidth: 12,
      backgroundBorderWidth: 12,
      backgroundColor: '#e1e1e1',
      foregroundColor: '#2d4b6f',
      animateInView: true,
      textColor: '#d1ad3c',
      fontColor: '#a1a1a1',
      percent: 46,
    });

    $("#expns-prg5").circliful({
      animationStep: 5,
      foregroundBorderWidth: 12,
      backgroundBorderWidth: 12,
      backgroundColor: '#e1e1e1',
      foregroundColor: '#2d4b6f',
      animateInView: true,
      textColor: '#d1ad3c',
      fontColor: '#a1a1a1',
      percent: 60,
    });

    $("#expns-prg6").circliful({
      animationStep: 5,
      foregroundBorderWidth: 12,
      backgroundBorderWidth: 12,
      backgroundColor: '#e1e1e1',
      foregroundColor: '#2d4b6f',
      animateInView: true,
      textColor: '#d1ad3c',
      fontColor: '#a1a1a1',
      percent: 50,
    });
  }

  //===== Count Down =====//
  if ($.isFunction($.fn.downCount)) {
    $('.cwnt-tim').downCount({
      date: '12/12/2019 12:00:00',
      offset: +5
    });
  }

  //===== Owl Carousel =====//
  if ($.isFunction($.fn.owlCarousel)) {

    //=== Featured Area Carousel ===//
    $('.featured-area').owlCarousel({
      autoplay: true,
      smartSpeed: 2000,
      loop: true,
      items: 1,
      dots: false,
      slideSpeed: 15000,
      autoplayHoverPause: true,
      nav: false,
      margin: 0,
      animateIn: 'fadeIn',
      animateOut: 'fadeOut',
      navText: [
      "<i class='fa fa-angle-up'></i>",
      "<i class='fa fa-angle-down'></i>"
      ]
    });

    //=== Featured Area Style 2 Carousel ===//
    $('.featured-area2').owlCarousel({
      autoplay: true,
      smartSpeed: 2000,
      loop: true,
      items: 1,
      dots: true,
      slideSpeed: 15000,
      autoplayHoverPause: true,
      nav: true,
      margin: 0,
      animateIn: 'fadeIn',
      animateOut: 'fadeOut',
      navText: [
      "<i class='flaticon-left-arrow'></i>",
      "<i class='flaticon-right-arrow'></i>"
      ]
    });

    //=== Testimonials Carousel ===//
    $('.testi-car').owlCarousel({
      autoplay: true,
      smartSpeed: 2000,
      loop: true,
      items: 1,
      dots: false,
      slideSpeed: 15000,
      autoplayHoverPause: true,
      nav: false,
      margin: 0,
      animateIn: 'fadeIn',
      animateOut: 'fadeOut',
      navText: [
      "<i class='fa fa-angle-up'></i>",
      "<i class='fa fa-angle-down'></i>"
      ]
    });
    
  }

})(window.jQuery);//===== Document Ready Ends =====//


$(window).on('load',function(){
  'use strict';
  $('.pageloader-wrap').fadeOut('slow');
  
  var header_height2 = $('header.style2').innerHeight();
  $('main').css({'padding-top': header_height2});


  //===== Isotope =====//
  if (jQuery('.fltr-itm').length > 0) {
    if (jQuery().isotope) {
      var jQuerycontainer = jQuery('.masonry'); // cache container
      jQuerycontainer.isotope({
        itemSelector: '.fltr-itm',
        columnWidth: 1,
        layoutMode: 'fitRows',
      });
	  jQuery('.fltr-lnks a').on('click',function () {
        var selector = jQuery(this).attr('data-filter');
        jQuery('.fltr-lnks li').removeClass('active');
        jQuery(this).parent().addClass('active');
        jQuerycontainer.isotope({ filter: selector });
        return false;
      });
      jQuerycontainer.isotope('layout'); // layout/layout
    }

	jQuery(window).on('resize',function () {
      if (jQuery().isotope) {
        jQuery('.masonry').isotope('layout'); // layout/relayout on window resize
      }
    });
  }
});//===== Window onLoad Ends =====//

//===== Sticky Header =====//
$(window).on('scroll',function () {
  'use strict';

  var header_height = $('header').innerHeight();

  var scroll = $(window).scrollTop();
  if (scroll >= header_height) {
    $('header').addClass('sticky-active');
  } else {
    $('header').removeClass('sticky-active');
  }
});//===== Window onScroll Ends =====//
