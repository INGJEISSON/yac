import React, { Component } from 'react';
import './App.css';
import { BrowserRouter } from 'react-router-dom'
import { Route } from 'react-router-dom'
import ChatRoomsList from './components/ChatRoomList'
import MessagesList from './components/MessagesList'
import UserService from './services/UserService';



const BaseLayout = () => (
  <div className="container">
    <nav className="navbar navbar-expand-lg navbar-light bg-light">
      <a className="navbar-brand" href="#">YAC - Yet Another Chat</a>
      <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span className="navbar-toggler-icon"></span>
      </button>
      <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div className="navbar-nav">
          <a className="nav-item nav-link" href="/">Salir</a>
          <a className="nav-item nav-link" href="/customer">Crear Canal</a>
        </div>
      </div>
    </nav>
    <div className="messaging">
      <div className="inbox_msg">
        <div className="inbox_people">

          <div className="headind_srch">
            <div className="recent_heading">
              <h4>Chats</h4>
            </div>
          </div>
          <Route path="/" exact component={ChatRoomsList} />
        </div>

        <div className="mesgs">

          <Route path="/" exact component={MessagesList} />

          <div className="type_msg">
            <div className="input_msg_write">
              <input type="text" className="write_msg" placeholder="Type a message" />
              <button className="msg_send_btn" type="button"><i className="fa fa-paper-plane-o" aria-hidden="true"></i></button>
            </div>
          </div>
        </div>
      </div>
      <p className="text-center top_spac"> Code <a target="_blank" href="https://github.com/cesarmauriciodr/yac">GitHub</a></p>
    </div>
  </div>
)

const userService = new UserService();

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      logged_in: localStorage.getItem('token') ? true : false,
      username: "",
      password: ""
    };
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleSubmit(event) {
    const data = {
      "username": this.state.username,
      "password": "pass1234"
    };

    var self = this;
    userService.authUser(data).then(function (result) {
      localStorage.setItem('token', result.data.token);
      self.setState({ logged_in: true })
    });
    event.preventDefault();
  }

  handleUserChange(event, self) {
    self.username = event.target.value
  }
  handlePasswordChange(e) {
    self.password = event.target.value
  }

  render() {
    if (this.state.logged_in) {
      return (
        <BrowserRouter>
          <BaseLayout />
        </BrowserRouter>
      );
    }
    else {
      return (
        <div className="container text-center">
          <form className="form-signin" onSubmit={e => this.handleSubmit(e, this.state)}>
            <img className="mb-4" src="./chat-icon.png" style={{ width: 150, paddingTop: 100 }} />
            <h1 className="h3 mb-3 font-weight-normal">Yet Another Chat</h1>
            <input type="text" onChange={e => this.handleUserChange(e, this.state)} className="form-control" required ></input>
            <input type="password" onChange={e => this.handlePasswordChange(e, this.state)} className="form-control" placeholder="Contraseña" required></input>
            <button className="btn btn-lg btn-primary btn-block" type="submit">Entrar</button>
          </form>
        </div>
      );
    }
  }
}
export default App;