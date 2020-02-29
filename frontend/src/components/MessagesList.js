import React, { Component } from 'react';
import MessageService from '../services/MessageService';


const messageService = new MessageService();

class MessageList extends Component {

    constructor(props) {
        super(props);
        this.state = {
            messages: []
        };
    }

    componentDidMount() {
        var self = this;
        messageService.messageList().then(function (result) {
            
            const messages = JSON.parse(result.get_chat);
            console.log(messages)
            self.setState({messages});
        });
    }

    render() {

        return (
            <div className="msg_history">
                
                {this.state.messages.map((item, key) =>
                    <div className="incoming_msg" key={item} >
                        
                        <div className="incoming_msg_img"> <img src="https://ptetutorials.com/images/user-profile.png" alt="sunil" /> </div>
                        <div className="received_msg">
                            <div className="received_withd_msg">
                                <p>{item.content}</p>
                                <span className="time_date">{item.send_at}</span>
                            </div>
                        </div>
                    </div>
                )}
            </div>
        );
    }
}
export default MessageList;
