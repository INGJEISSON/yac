import React, { Component } from 'react';
import ChatRoomsService from '../services/ChatRoomService';


const chatRoomsService = new ChatRoomsService();

class ChatRoomsList extends Component {

    constructor(props) {
        super(props);
        this.state = {
            chat_room: []
        };
    }

    componentDidMount() {
        var self = this;
        chatRoomsService.getChatRooms().then(function (result) {
            const chat_room = result.results;
            self.setState({ chat_room });
        });
    }

    render() {

        return (
            <div className="inbox_chat">
                {this.state.chat_room.map(c =>
                    <div className="chat_list active_chat" key={c.id}>
                        <div className="chat_people">
                            
                            <div className="chat_img">
                                <img src="./chat-icon.jpg" alt="sunil" />
                            </div>
                            <div className="chat_ib">
                                <h5>
                                    {c.name}
                                    <span className="chat_date">Miembros: {c.get_users_online}</span>
                                </h5>
                                <p>{c.description}</p>
                            </div>
                        </div>
                    </div>
                )}
            </div>

        );
    }
}
export default ChatRoomsList;
