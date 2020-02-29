import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class ChatRoomsService {

    constructor() { }

    getChatRooms() {
        const url = `${API_URL}/api/chat_rooms/`;
        return axios.get(url).then(response => response.data);
    }

    getChatRoom(pk) {
        const url = `${API_URL}/api/chat_rooms/${pk}`;
        return axios.get(url).then(response => response.data);
    }

    createChatRoom(chat_room) {
        const url = `${API_URL}/api/chat_rooms/`;
        return axios.post(url, chat_room);
    }
}