import React from "react"
import {Link, useParams} from "react-router-dom"

const MessageItem = ({message, dispatches, clients, delete_message}) => {
    // Find the corresponding dispatch and client objects
    const dispatch = dispatches.find((d) => d.uu_id === message.dispatch);
    const client = clients.find((c) => c.uu_id === message.client);

    return (
        <tr>
            <td>{message.id}</td>
            <td>{message.send_status ? "Отправлено" : "Не отправлено"}</td>
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

const DispatchDetails = ({dispatches, messages}) => {
    const params = useParams();
    const filtered_dispatch = dispatches.find((dispatch) => dispatch.uu_id === params.uu_id);
    const filtered_messages = messages.filter((message) => message.dispatch === filtered_dispatch?.uu_id);
    return (
        <div className="section is-medium">
            <p className="title">
                Список сообщений рассылки: {filtered_dispatch?.uu_id}
            </p>
            <p className="subtitle">
                таблица созданных сообщений
            </p>
            <table className="table is-narrow is-fullwidth">
                <thead className="has-background-info-light">
                <th>ID сообщения</th>
                <th>Статус отправки</th>
                <th>Старт рассылки</th>
                <th>Финиш рассылки</th>
                <th>Номер клиента</th>
                </thead>
                {filtered_messages.map((message)=> <MessageItem message={message}/>)}
            </table>
            <Link class='button is-light' to='/dispatches/create'>Создать рассылку</Link>
        </div>
    )
}

export default DispatchDetails;