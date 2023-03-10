$('#myModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
  })

function add_classroom(){
    var name = prompt("Enter the Classname : ");
    var cls = document.querySelector(".classroom_list");
    var cont = document.createElement("div");
    cont.classList.add("card");
    var horizontal = document.createElement("hr");
    cont.innerHTML = name;
    cont.appendChild(horizontal);
    cls.appendChild(cont);
    body.appendChild(cls);
    $('#myModal').on('shown.bs.modal', function () {
        $('#myInput').trigger('focus')
    })
}