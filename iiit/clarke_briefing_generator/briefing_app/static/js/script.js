

// drag & drop upload

const dropArea = document.getElementById("dropArea");
const fileInput = document.getElementById("fileInput");

dropArea.addEventListener("dragover", e=>{
e.preventDefault();
dropArea.style.background="rgba(255,255,255,0.1)";
});

dropArea.addEventListener("dragleave", ()=>{
dropArea.style.background="transparent";
});

dropArea.addEventListener("drop", e=>{
e.preventDefault();
fileInput.files = e.dataTransfer.files;
dropArea.style.background="transparent";
});


// progress bar

const form = document.getElementById("uploadForm");
const progressContainer = document.getElementById("progressContainer");
const progressBar = document.getElementById("progressBar");

form.addEventListener("submit", ()=>{

progressContainer.style.display="block";

let progress = 0;

let interval = setInterval(()=>{

progress += 5;

progressBar.style.width = progress + "%";

if(progress >= 90){
clearInterval(interval);
}

},300);

});


// AI typing animation

const output = document.getElementById("aiOutput");

if(output){

let text = output.innerText;

output.innerText = "";

let i = 0;

function typeWriter(){

if(i < text.length){

output.innerText += text.charAt(i);
i++;

setTimeout(typeWriter,15);

}

}

typeWriter();

}