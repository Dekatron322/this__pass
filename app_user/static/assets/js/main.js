$('#toogleIcon1').click(function () {
    $('#icon1').toggleClass('fa-caret-right').toggleClass('fa-caret-down');
});

$('#toogleIcon2').click(function () {
    $('#icon2').toggleClass('fa-caret-right').toggleClass('fa-caret-down');
});

$('#toogleIcon3').click(function () {
    $('#icon3').toggleClass('fa-caret-right').toggleClass('fa-caret-down');
});

$('#toggleSummary').click(function () {
    $('#summary-icon').toggleClass('fa-chevron-up').toggleClass('fa-chevron-down');
      $("#toggleSummary #summary-btn-text").text($("#toggleSummary #summary-btn-text").text() == 'Show order summary' ? 'Hide order summary' : 'Show order summary');
});

// $('.card-selector').click(function(event) {
//   $('.card-selector').not(this).removeClass('card-clicked');
//   $(this).toggleClass('card-clicked');
// });


(function () {
    "use strict";
    var jQueryPlugin = (window.jQueryPlugin = function (ident, func) {
        return function (arg) {
            if (this.length > 1) {
                this.each(function () {
                    var $this = $(this);

                    if (!$this.data(ident)) {
                        $this.data(ident, func($this, arg));
                    }
                });

                return this;
            } else if (this.length === 1) {
                if (!this.data(ident)) {
                    this.data(ident, func(this, arg));
                }

                return this.data(ident);
            }
        };
    });
})();

(function () {
    "use strict";
    function Quantity($root) {
        const element = $root;
        const quantity = $root.first("data-quantity");
        const quantity_target = $root.find("[data-quantity-target]");
        const quantity_minus = $root.find("[data-quantity-minus]");
        const quantity_plus = $root.find("[data-quantity-plus]");
        var quantity_ = quantity_target.val();
        $(quantity_minus).click(function () {
            quantity_target.val(--quantity_);
        });
        $(quantity_plus).click(function () {
            quantity_target.val(++quantity_);
        });
    }
    $.fn.Quantity = jQueryPlugin("Quantity", Quantity);
    $("[data-quantity]").Quantity();
})();


function cardChange(elem) {
    let card = document.getElementById('card-preview');

    if (elem.id === 'black-btn') {
        card.classList.toggle('blackCard');
        card.classList.remove('whiteCard', 'greyCard');

        elem.parentNode.classList.toggle('card-clicked');
        document.getElementsByClassName("card-selector")[1].classList.remove("card-clicked");
        document.getElementsByClassName("card-selector")[2].classList.remove("card-clicked");

        $("#card-change-name").val("ThisPass Black Card");

    } else if (elem.id === 'grey-btn') {
        card.classList.toggle('greyCard');
        card.classList.remove('blackCard', 'whiteCard');

        elem.parentNode.classList.toggle('card-clicked');
        document.getElementsByClassName("card-selector")[0].classList.remove("card-clicked");
        document.getElementsByClassName("card-selector")[2].classList.remove("card-clicked");

        $("#card-change-name").val("ThisPass Grey Card");

    } else {
        card.classList.toggle('whiteCard');
        card.classList.remove('blackCard', 'greyCard');

        elem.parentNode.classList.toggle('card-clicked');
        document.getElementsByClassName("card-selector")[0].classList.remove("card-clicked");
        document.getElementsByClassName("card-selector")[1].classList.remove("card-clicked");

        $("#card-change-name").val("ThisPass White Card");

    }

    const classExists = document.getElementsByClassName('card-clicked').length > 0;

    if (!classExists) {
        $("#card-change-name").val("");
    }
}




// const alertPlaceholder = document.getElementById('liveAlertPlaceholder');
//           const bsAlert = bootstrap.Alert.getOrCreateInstance('#liveAlertPlaceholder');

// const alert = (message, type) => {
//   const wrapper = document.createElement('div')
//   wrapper.innerHTML = [      
//       `<div class="alert alert-${type} text-center w-100" role="alert"><span>${message}</span></div>`
//   ].join('')

//   alertPlaceholder.append(wrapper)
// }

// const alertTrigger = document.getElementById('loginBtn')
// if (alertTrigger) {
//   alertTrigger.addEventListener('click', () => {
//     alert('Invalid Email or Password', 'danger');
//       setTimeout(function(){
// bsAlert.close();
// }, 5000);
//   })
// }
