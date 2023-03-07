function returnHome() {
    window.location.href = '/';
}

function replyMessage(id) {
    window.location.href = `/message/${id}/reply`;
}

function forwardMessage(id) {
    window.location.href = `/message/${id}/forward`;
}
