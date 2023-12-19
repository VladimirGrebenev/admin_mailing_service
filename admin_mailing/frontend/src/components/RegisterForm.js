import React, {useState} from "react";
import axios from "axios";

const RegisterForm = () => {
    const [user, setUser] = useState({
        user_name: "",
        email: "",
        password: ""
    });

    const handleChange = (e) => {
        setUser({...user, [e.target.name]: e.target.value});
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        axios
            .post("http://127.0.0.1:8000/users/register/", user)
            .then((response) => {
                console.log(response.data);
                this.props.get_token(user.email, user.password)
            })
            .catch((error) => {
                console.log(error);
                // Добавьте здесь код для обработки ошибки регистрации
            });
    };

    return (
        <div className="section">
            <h1 className="title" style={{textAlign: "center"}}>Register</h1>
            <div className="columns">
                <div className="column"></div>
                <div className="column is-one-third">
                    <form onSubmit={handleSubmit}>
                        <div className="field">
                            <label className="label">Имя пользователя:</label>
                            <div className="control">
                                <input name="user_name" className="input"
                                       type="text" placeholder="your nickname"
                                       value={user.user_name}
                                       onChange={handleChange}/>
                            </div>
                        </div>
                        <div className="field">
                            <label className="label">Email:</label>
                            <div className="control">
                                <input name="email"
                                       className="input" type="email"
                                       placeholder="email@email.com"
                                       value={user.email}
                                       onChange={handleChange}/>
                            </div>
                        </div>
                        <div className="field">
                            <label className="label">Пароль:</label>
                            <div className="control">
                                <input name="password"
                                       className="input" type="password"
                                       placeholder="strong password"
                                       value={user.password}
                                       onChange={handleChange}/>
                            </div>
                        </div>
                        <div className="field">
                            <input className="button is-success" type="submit"
                                   value="Создать"/>
                        </div>
                    </form>
                </div>
                <div className="column"></div>
            </div>
        </div>
    );
};

export default RegisterForm;