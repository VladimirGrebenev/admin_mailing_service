import React from "react";
import axios from "axios";

class RegisterUser extends React.Component {
    constructor(props) {
        super();
        this.state = {user_name: '', email: '', password: ''};
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }


    handleSubmit(event) {
        event.preventDefault();
        const {user_name, email, password} = this.state;

        // Проверка на пустые значения
        if (!user_name || !email || !password) {
            alert("Пожалуйста, заполните все поля");
            return;
        }

        const user = {
            user_name: user_name,
            email: email,
            password: password
        };

        axios
            .post("http://127.0.0.1:8000/users/register/", user)
            .then((response) => {
                console.log(response.data);
                alert('Вы зарегистрировались по почте: ' + email);
                this.props.get_token(email, password);
            })
            .catch((error) => {
                console.log(error);
                alert('что-то пошло не так, попробуй ещё раз');
                // Добавьте здесь код для обработки ошибки регистрации
            });
    };

    render() {
        return (
            <div className="section">
                <h1 className="title"
                    style={{textAlign: "center"}}>Register</h1>
                <div className="columns">
                    <div className="column"></div>
                    <div className="column is-one-third">
                        <form onSubmit={(event) => this.handleSubmit(event)}>
                            <div className="field">
                                <label className="label">Имя
                                    пользователя:</label>
                                <div className="control">
                                    <input name="user_name" className="input"
                                           type="text"
                                           placeholder="your nickname"
                                           value={this.state.user_name}
                                           onChange={(event) => this.handleChange(event)}/>
                                </div>
                            </div>
                            <div className="field">
                                <label className="label">Email:</label>
                                <div className="control">
                                    <input name="email"
                                           className="input" type="email"
                                           placeholder="email@email.com"
                                           value={this.state.email}
                                           onChange={(event) => this.handleChange(event)}/>
                                </div>
                            </div>
                            <div className="field">
                                <label className="label">Пароль:</label>
                                <div className="control">
                                    <input name="password"
                                           className="input" type="password"
                                           placeholder="strong password"
                                           value={this.state.password}
                                           onChange={(event) => this.handleChange(event)}/>
                                </div>
                            </div>
                            <div className="field">
                                <input className="button is-success"
                                       type="submit"
                                       value="Создать"/>
                            </div>
                        </form>
                    </div>
                    <div className="column"></div>
                </div>
            </div>
        );
    };
}

export default RegisterUser;