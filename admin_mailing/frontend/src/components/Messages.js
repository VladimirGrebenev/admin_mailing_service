import React from "react"
import {Link} from "react-router-dom";

const MessageItem = ({message, delete_message}) => {
    return (
        <tr>
            <td>{message.send_status}</td>
            <td>{message.dispatch.uu_id}</td>
            <td>{message.dispatch.start_datetime}</td>
            <td>{message.dispatch.end_datetime}</td>
            <td>{message.client.phone_number}</td>
            <td>
                <button className='button is-danger' type='button'
                        onClick={() => delete_message(message.id)}>Удалить
                </button>
            </td>
        </tr>
    )
}

const MessagesList = ({messages, delete_message}) => {
    return (
        <div className="section is-medium">
            <p className="title">
                Список cообщений в рассылках
            </p>
            <p className="subtitle">
                таблица созданных сообщений
            </p>
            <table className="table is-narrow is-fullwidth">
                <thead className="has-background-info-light">
                <th>Статус отправки</th>
                <th>Номер рассылки</th>
                <th>Старт рфссылки</th>
                <th>Финиш рассылки</th>
                <th>Номер клиента</th>
                <th></th>
                </thead>
                {messages.map((message)=> <MessageItem message={message} delete_message={delete_message}/>)}
            </table>
            <Link class='button is-light' to='/messages/create'>Создать сообщение</Link>
        </div>
    )
}

export default MessagesList