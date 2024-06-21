
    function getFecha(){
        const d = new Date();
        let text = d.toString();
        return text;
    }

    function Ir(cual){
        document.forms['mio'].action="/registrarAprendizcoordinacion/"+cual
        document.forms['mio'].submit();
     
     
       }function Ir1(cual){
        location.href=cual
       }
        function Confirmar(que,donde){
            if (confirm(que))
              location.href=donde
        }
       function Va(tipo){
        
        if(tipo=="i")
        document.forms['mio'].action="/registrarAprendizcoordinacion/i"
        
        
        document.forms['mio'].submit();    
     
       }

       function Ir2(cual){
        document.forms['mio'].action="/reportarAprendizcoordinacion/"+cual
        document.forms['mio'].submit();
     
     
       }function Ir1(cual){
        location.href=cual
       }
        function Confirmar(que,donde){
            if (confirm(que))
              location.href=donde
        }

       function Va1(tipo){
        
        if(tipo=="i")
        document.forms['mio'].action="/reportarAprendizcoordinacion/i"
        
        
        document.forms['mio'].submit();    
     
       }

       
    
    

    function mostrarCampos(){
        var rol = document.getElementById("Rol").value; 
        var camposAprendiz = document.getElementById("camposAprendiz");

        if (rol =='Aprendiz'){
            camposAprendiz.style.display ="block";
        }
        else{
            camposAprendiz.style.display="none";
        }
    }

    function mostrarcampoFalta(){
        var falta =document.getElementById("Falta").value;
        var Otro = document.getElementById("Otro")

        if(falta =='Otro'){
            Otro.style.display="block";
        }
        else{
            Otro.style.display="none"
        }
    }

