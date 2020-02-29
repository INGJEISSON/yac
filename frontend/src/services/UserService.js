import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class UserService {

    constructor() { }

    authUser(data) {
        const url = `${API_URL}/api-token-auth/`;
        return axios.post(url, data, {headers: {'Content-Type': 'application/json'}})
    }


    getUser(chat_room) {
        const id = localStorage.getItem('id');
        const url = `${API_URL}/api/chat_rooms/${id}`;
        return axios.post(url, chat_room);
    }
}


