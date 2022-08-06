const nxtBtn = document.querySelector('#submitBtn');
const form1 = document.querySelector('#form1');
const form2 = document.querySelector('#form2');
const form3 = document.querySelector('#form3');

var viewId = 1;
function nextForm() {
    console.log("hellonext");
    viewId = viewId + 1;
    displayForms();

    console.log(viewId);

}

function prevForm() {
    console.log("helloprev");
    viewId = viewId - 1;
    displayForms();

    console.log(viewId);
}

function displayForms() {

    if (viewId > 3) {
        viewId = 3;
    }

    if (viewId === 1) {
        form1.style.display = 'block';
        form2.style.display = 'none';
        form3.style.display = 'none';


    } else if (viewId === 2) {
        form1.style.display = 'none';
        form2.style.display = 'block';
        form3.style.display = 'none';

    } else if (viewId === 3) {
        form1.style.display = 'none';
        form2.style.display = 'none';
        form3.style.display = 'block';

    }
}