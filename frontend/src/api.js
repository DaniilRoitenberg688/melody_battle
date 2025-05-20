
// let host = "http://localhost:5000/api";
let host = "/api"

async function register(userData){
    let request = await fetch(host + '/user/register', {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(userData)})
    let status_code = request.status;
    console.log(status_code);
    let data = await request.json();
    console.log(data);
    return {data: data, status_code: status_code};
}

async function login(userData){
    let request = await fetch(host + '/user/login', {method: "POST",headers: { "Content-Type": "application/json" },body: JSON.stringify(userData)})
    let status_code = request.status;
    let data = await request.json();
    console.log({data: data, status_code: status_code})
    return {data: data, status_code: status_code};
}

async function getUser(token){
    let request = await fetch(host + '/user', {method: "GET",headers: {"Authorization": `Bearer ${token}`}})
    let status_code = request.status;
    let data = await request.json();
    return {data: data, status_code: status_code};
}

async function createMelodyBattleApi(token, url){
    let request = await fetch(host + '/melody_battle', {method: "POST",headers: {"Authorization": `Bearer ${token}`, 'Content-Type': 'application/json'}, body: JSON.stringify({'url': url})})
    let status_code = request.status;
    let data = await request.json();
    return {data: data, status_code: status_code};
}

async function getMelodyBattleApi(token){
    let request = await fetch(host + '/melody_battle', {method: "GET",headers: {"Authorization": `Bearer ${token}`}})
    let status_code = request.status;
    let data = await request.json();
    return {data: data, status_code: status_code};
}

export {register, login, getUser, createMelodyBattleApi, getMelodyBattleApi, host};
