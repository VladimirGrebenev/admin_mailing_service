import React from "react";
import {BrowserRouter, Link, Redirect, Route, Switch} from "react-router-dom";
import Cookies from "universal-cookie";
import axios from "axios";

import ClientList from "./components/Clients";
import DispatchesList from "./components/Dispatches";
import MessagesList from "./components/Messages";
import MenuList from "./components/Menu";
import AddFooter from "./components/Footer";
import DispatchDetails from "./components/DispatchDetails";
import ClientDispatches from "./components/ClientDispatches";
import DispatchStatistics from "./components/DispatchStatistics";
import RegisterForm from "./components/RegisterForm";
import LoginForm from "./components/Auth";
import DispatchForm from "./components/DispatchForm";
import ClientForm from "./components/ClientForm";


const NotFound404 = ({location}) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'clients': [],
            'dispatches': [],
            'messages': [],
            'menu_links': [],
            'token': '',
            'email': '',
            'authorized_user': '',
        }
    }

    set_token(token, email = '') {
        const cookies = new Cookies()
        cookies.set('token', token, {maxAge: 3600})
        cookies.set('email', email, {maxAge: 3600})
        this.setState({'token': token, 'email': email}, () => this.load_data())
        window.location.href = "/"
    }

    is_authenticated() {
        return this.state.token !== ''
    }

    logout() {
        this.set_token('')
        window.location.reload();
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        const email = cookies.get('email')
        this.setState({'token': token, 'email': email}, () => this.load_data())
    }

    get_token(email, password) {
        axios.post('http://127.0.0.1:8000/token-api-auth/', {
            username: email,
            password: password
        })
            .then(response => {
                this.set_token(response.data['token'], email)
                alert('Вы авторизовались по почте: ' + email)
            }).catch(error => alert('Неверный логин или пароль'))
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_authenticated()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }

    load_data() {
        const headers = this.get_headers();

        axios.get('http://127.0.0.1:8000/clients/', {headers})
            .then(response => {
                this.setState({clients: response.data.results});
            }).catch(error => console.log(error));

        axios.get('http://127.0.0.1:8000/dispatches/', {headers})
            .then(response => {
                this.setState({dispatches: response.data.results})
                console.log(response.data.results)
            }).catch(error => console.log(error));

        axios.get('http://127.0.0.1:8000/messages/', {headers})
            .then(response => {
                this.setState({messages: response.data.results})
            }).catch(error => console.log(error));

        this.load_menu();
    }


    get_login_link() {
        if (this.is_authenticated()) {
            return (
                <p>
                    <button
                        className="button is-primary">{this.state.email}</button>
                    <button className="button is-light"
                            onClick={() => this.logout()}>Log out
                    </button>
                </p>
            )
        } else {
            return (
                <p>
                    <button className="button is-primary">@guest</button>
                    <Link to="/login" className="button is-link">Login</Link>
                    <Link to="/register" className="button is-warning">Register</Link>
                </p>
            );
        }
    }

    load_menu() {
        let is_auth_link = this.get_login_link()
        const menu_links = [
            {
                'link_name': 'Рассылки',
                'menu_link': '/dispatches'
            },
            {
                'link_name': 'Сообщения',
                'menu_link': '/messages'
            },
            {
                'link_name': 'Клиенты',
                'menu_link': '/clients'
            },
            {
                'link_name': 'Статистика',
                'menu_link': '/statistics'
            },
        ]

        this.setState(
            {'menu_links': menu_links, 'is_auth_link': is_auth_link}
        )
    }

    componentDidMount() {
        this.get_token_from_storage()
    }

    delete_dispatch(uu_id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/dispatches/${uu_id}`, {headers})
            .then(response => {
                this.setState({
                    dispatches: this.state.dispatches.filter((item) => item
                        .uu_id !== uu_id)
                })
            }).catch(error => console.log(error))
    }

    delete_message(id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/messages/${id}`, {headers})
            .then(response => {
                this.setState({
                    messages: this.state.messages.filter((item) => item.id !==
                        id)
                })
            }).catch(error => console.log(error))
    }

    delete_client(uu_id) {
        const headers = this.get_headers()
        axios.delete(`http://127.0.0.1:8000/clients/${uu_id}`, {headers})
            .then(response => {
                this.setState({
                    clients: this.state.clients.filter((item) => item
                        .uu_id !== uu_id)
                })
            }).catch(error => console.log(error))
    }

    createDispatch(start_datetime, end_datetime, message_text, tag_filter, operator_code_filter) {
        const headers = this.get_headers();
        const data = {
            start_datetime: start_datetime,
            end_datetime: end_datetime,
            message_text: message_text,
            tag_filter: tag_filter,
            operator_code_filter: operator_code_filter
        };

        axios.post(`http://127.0.0.1:8000/dispatches/`, data, {headers})
            .then(response => {
                let new_dispatch = response.data;
                this.setState(prevState => ({
                    dispatches: prevState.dispatches.concat(new_dispatch)
                }));
            })
            .catch(error => console.log(error));

        window.location.href = "/dispatches";
    }

    createClient(phone_number, operator_code, tag, timezone) {
        const headers = this.get_headers();
        const data = {
            phone_number: phone_number,
            operator_code: operator_code,
            tag: tag,
            timezone: timezone,
        };

        axios.post(`http://127.0.0.1:8000/clients/`, data, {headers})
            .then(response => {
                let new_client = response.data;
                this.setState(prevState => ({
                    clients: prevState.clients.concat(new_client)
                }));
            })
            .catch(error => console.log(error));

        window.location.href = "/clients";
    }

    createMessage(send_status, dispatch, client) {
        const headers = this.get_headers()
        const data = {
            send_status: send_status,
            dispatch: dispatch,
            client: client
        }
        axios.post(`http://127.0.0.1:8000/messages/`, data, {headers})
            .then(response => {
                let new_message = response.data
                const dispatch = this.state.dispatches.filter((item) => item
                    .uu_id === new_message.dispatch)[0]
                new_message.dispatch = dispatch
                this.setState({messages: [...this.state.messages, new_message]})
            }).catch(error => console.log(error))
        window.location.href = "/messages"
    }


    render() {
        return (
            <div className="App">
                <BrowserRouter>
                    <MenuList menu_links={this.state.menu_links}
                              is_auth={this.state.is_auth_link}/>
                    <Switch>
                        <Route exact path='/dispatches'
                               component={() => <DispatchesList
                                   dispatches={this.state.dispatches}
                                   delete_dispatch={(uu_id) => this.delete_dispatch(uu_id)}/>}/>
                        <Route exact path="/messages"
                               component={() => <MessagesList
                                   messages={this.state.messages}
                                   dispatches={this.state.dispatches}
                                   clients={this.state.clients}
                                   delete_message={(id) => this.delete_message(id)}/>}/>
                        <Route exact path='/clients'
                               component={() => <ClientList clients={this.state.clients}
                               delete_client={(uu_id) => this.delete_client(uu_id)}/>}/>
                        <Route exact path='/statistics'
                               component={() => <DispatchStatistics
                                   dispatches={this.state.dispatches}
                                   messages={this.state.messages}/>}/>
                        <Route exact path='/login' component={() => <LoginForm
                            get_token={(username, password) => this.get_token(username, password)}/>}/>
                        <Route path="/register" component={() => <RegisterForm
                            get_token={(username, password) => this.get_token(username, password)}/>}/>
                        <Route exact path='/clients/create'
                               component={() => <ClientForm
                                   clients={this.state.clients}
                                   createClient={(phone_number, operator_code, tag, timezone) => this.createClient(phone_number, operator_code, tag, timezone)}/>}/>
                        <Route exact path='/dispatches/create'
                               component={() => <DispatchForm
                                   dispatches={this.state.dispatches}
                                   messages={this.state.messages}
                                   clients={this.state.clients}
                                   createDispatch={(start_datetime, end_datetime, message_text, tag_filter, operator_code_filter) => this.createDispatch(start_datetime, end_datetime, message_text, tag_filter, operator_code_filter)}/>}/>
                        <Route exact path='/clients/:uu_id'
                               component={() => <ClientDispatches
                                   clients={this.state.clients}
                                   dispatches={this.state.dispatches}/>}/>
                        <Route exact path='/dispatches/:uu_id'
                               component={() => <DispatchDetails
                                   messages={this.state.messages}
                                   clients={this.state.clients}
                                   dispatches={this.state.dispatches}/>}/>

                        <Redirect from='/' to='/dispatches'/>
                        <Route component={NotFound404}/>
                    </Switch>
                </BrowserRouter>
                <AddFooter/>
            </div>
        )
    }
}

export default App;