import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class MessageList {

    constructor() { }

    messageList() {
        const url = `${API_URL}/api/chat_room/1`;
        return axios.get(url).then(response => response.data);
    }

}


