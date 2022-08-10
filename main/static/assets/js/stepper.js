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

const dropArea = document.querySelector(".drag-image"),
    dropbutton = dropArea.querySelector("#profileImgBtn"),
    dropInput = dropArea.querySelector("#profileImg");
let dropFile;

dropbutton.onclick = () => {
    dropInput.click();
}

dropInput.addEventListener("change", function () {
    dropFile = this.files[0];
    dropArea.classList.add("active");
    viewfile();
});

dropArea.addEventListener("dragover", (event) => {
    event.preventDefault();
    dropArea.classList.add("active");
    dropbutton.textContent = "Release to Upload Image";
});

dropArea.addEventListener("dragleave", () => {
    dropArea.classList.remove("active");
    dropbutton.textContent = "Browse Images";
});

dropArea.addEventListener("drop", (event) => {
    event.preventDefault();
    dropFile = event.dataTransfer.files[0];
    viewfile();
});

function viewfile() {
    let fileType = dropFile.type;
    let validExtensions = ["image/jpeg", "image/jpg", "image/png"];
    if (validExtensions.includes(fileType)) {
        let fileReader = new FileReader();
        fileReader.onload = () => {
            let fileURL = fileReader.result;
            let imgTag = `<img src="${fileURL}" alt="image">`;
            dropArea.innerHTML = imgTag;
            dropArea.style.height = "250px";
        }
        fileReader.readAsDataURL(dropFile);
    } else {
        alert("This is not an Image File!");
        dropArea.classList.remove("active");
        dragText.textContent = "Drag & Drop to Upload File";
    }
}