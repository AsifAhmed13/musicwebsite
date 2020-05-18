document.addEventListener('DOMContentLoaded',function(){
    const Signin = document.getElementById('Sign in');
    Signin.onclick = function(){
        var s = window.location.href.split('/');
        s.pop();
        s = s.join('/');
        window.location.href = s;
    } 
});