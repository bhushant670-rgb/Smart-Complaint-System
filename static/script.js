function submitComplaint(){

let name = document.getElementById("name").value;

let room = document.getElementById("room").value;

let complaint = document.getElementById("complaint").value;


let data = {

name:name,

room:room,

complaint:complaint

};


localStorage.setItem("complaint", JSON.stringify(data));


alert("Complaint Saved Successfully");

}