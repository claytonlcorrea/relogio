function atualizarRelogio() {
    const agora = new Date();

    const horas = agora.getHours();
    const minutos = agora.getMinutes();
    const segundos = agora.getSeconds();

    const grausHoras = (horas % 24) * 15 + (minutos / 60) * 15; // 15 graus por hora, 0.25 graus por minuto
    const grausMinutos = minutos * 6 + (segundos / 60) * 6; // 6 graus por minuto, 0.1 grau por segundo
    const grausSegundos = segundos * 6; // 6 graus por segundo

    document.getElementById('ponteiroHoras').style.transform = `rotate(${grausHoras}deg)`;
    document.getElementById('ponteiroMinutos').style.transform = `rotate(${grausMinutos}deg)`;
    document.getElementById('ponteiroSegundos').style.transform = `rotate(${grausSegundos}deg)`;

    setTimeout(atualizarRelogio, 1000);
}

// Chame a função para iniciar o relógio
 atualizarRelogio();      
 window.onload = atualizarRelogio;