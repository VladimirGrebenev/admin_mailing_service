import React from "react"
import {Link} from "react-router-dom";

const MessageItem = ({message, dispatches, clients, delete_message}) => {
    // Find the corresponding dispatch and client objects
    const dispatch = dispatches.find((d) => d.uu_id === message.dispatch);
    const client = clients.find((c) => c.uu_id === message.client);

    return (
        <tr>
            <td>{message.id}</td>
            <td>{message.send_status ? "Отправлено" : "Не отправлено"}</td>
            <td>{message.dispatch}</td>
            <td>{dispatch.start_datetime}</td>
            <td>{dispatch.end_datetime}</td>
            <td>{client.phone_number}</td>
            <td>
                <button className='button is-danger' type='button'
                        onClick={() => delete_message(message.uu_id)}>Удалить
                </button>
            </td>
        </tr>
    )
}

const MessagesList = ({messages, clients, dispatches, delete_message}) => {
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
                <th>ID</th>
                <th>Статус отправки</th>
                <th>Номер рассылки</th>
                <th>Старт рассылки</th>
                <th>Финиш рассылки</th>
                <th>Номер клиента</th>
                <th></th>
                </thead>
                {messages.map((message)=> <MessageItem message={message} dispatches={dispatches} clients={clients} delete_message={delete_message}/>)}
            </table>
            <Link class='button is-light' to='/dispatches/create'>Создать  рассылку</Link>
        </div>
    )
}

export default MessagesList;