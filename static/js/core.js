document.getElementById('narutator').onclick = function(){
    file = document.getElementById('frmnaruto');
    file.click();
    
    alert(file.name);
}

document.getElementById('frmnaruto').oninput = function(){
    document.getElementById('btn-narutator').click();
}